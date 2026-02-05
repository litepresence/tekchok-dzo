import getpass
import os
import random
import shutil
import time
from random import random

import undetected_geckodriver as ug  # pip install undetected-geckodriver
from markdownify import markdownify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait

# =============================================================================
# CONFIGURATION
# =============================================================================
PROFILE_BASE = os.path.abspath("./firefox_stealth_logged_in_profile")
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0) Gecko/20100101 Firefox/130.0"
os.getlogin = lambda: getpass.getuser()
def grace_period():
    """
    Sleep for a small random period between 1 and 2 seconds
    to make delays less robotic
    """
    time.sleep(1 + random())


def log_in(site_url: str = "https://chat.mistral.ai"):
    """
    Run ONCE. Creates the profile directly in the final location → no broken symlinks.
    """
    if os.path.exists(PROFILE_BASE):
        print(f"Profile already exists at {PROFILE_BASE}")
        print("Delete the folder if you want to log in again.")
        return

    os.makedirs(PROFILE_BASE, exist_ok=True)

    print("Opening Firefox with the permanent profile folder...")
    options = _build_stealth_options(headless=False, profile_path=PROFILE_BASE)

    driver = ug.Firefox(options=options)
    driver.get(site_url)

    print("\nPlease log in manually (2FA, captcha, etc.)")
    input("When you are fully logged in → press Enter here...")

    driver.quit()
    print(f"Logged-in profile successfully saved to:\n{PROFILE_BASE}")
    print("You can now use create_context() forever!")


def create_context(headless: bool = True, fresh_copy: bool = True):
    if not os.path.exists(PROFILE_BASE):
        raise FileNotFoundError(f"Run log_in() first! Missing {PROFILE_BASE}")

    if fresh_copy:
        import tempfile
        profile_path = tempfile.mkdtemp(prefix="ff_stealth_")
        shutil.copytree(PROFILE_BASE, profile_path, dirs_exist_ok=True,
                        symlinks=False,  # ← ignore broken symlinks if any
                        ignore=shutil.ignore_patterns("parent.lock", "lock"))  # skip lock files
    else:
        profile_path = PROFILE_BASE

    options = _build_stealth_options(headless=headless, profile_path=profile_path)
    driver = ug.Firefox(options=options)

    driver.get("https://chat.mistral.ai/chat")
    return driver


def _build_stealth_options(headless: bool, profile_path: str):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument(f"--profile={profile_path}")
    options.binary_location = '/usr/bin/firefox'

    prefs = {
        "dom.webdriver.enabled": False,
        "useAutomationExtension": False,
        "general.useragent.override": USER_AGENT,
        "privacy.resistFingerprinting": True,
        "privacy.trackingprotection.enabled": True,
        "network.http.referer.XOriginPolicy": 0,
        "media.peerconnection.enabled": True,
        "webgl.disabled": False,
        "dom.storage.enabled": True,
        "browser.privatebrowsing.autostart": False,
    }
    for k, v in prefs.items():
        options.set_preference(k, v)

    return options


def create_new_chat(driver):
    print("creating new chat...")
    driver.get("https://chat.mistral.ai/chat")
    grace_period()


def responses_count_reaches(expected_count):
    def _predicate(driver):
        elements = driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Copy to clipboard']")
        return len(elements) >= expected_count if elements else False
    return _predicate


def ask_gpt(
    driver: webdriver.Firefox,
    prompt: str,
    timeout: int = 20,
    new_chat: bool = True,
):
    """
    Create a new chat on the context `driver`, set thinking and search to the
    given states, and ask mistral `prompt`.

    Timeout is given in minutes.

    Returns mistral's response as markdown.
    """
    try:
        if new_chat:
            create_new_chat(driver)

        grace_period()

        # Send message input
        print("sending message...")
        chat_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ProseMirror"))
        )
        driver.execute_script("arguments[0].innerHTML = arguments[1];", chat_input, prompt)
        grace_period()

        # Connec to send button
        send_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Send question']")
        send_button.click()

        print("waiting for mistral to finish...")
        # Wait until the chat container is present
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.CLASS_NAME, "markdown-container-style"))
        )
        # print("found response container")

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Stop generation']"))
        )
        # print("found stop button")
        WebDriverWait(driver, timeout*60).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Stop generation']"))
        )

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Rewrite']"))
        )
        # print("found regenerate button")

        grace_period()

        print("parsing response...")

        # Retrieve the raw HTML of that element
        raw_html = driver.find_elements(By.CLASS_NAME, "markdown-container-style")[-1].get_attribute("innerHTML")

        markdown = markdownify(raw_html)

        return markdown
    except:
        driver.quit()
        raise


def test():
    driver = create_context(True)
    resp = ask_gpt(driver, "Why is the sky green?")
    print(resp)
    resp = ask_gpt(driver, "Are you quite sure?", new_chat=False)
    print(resp)
    driver.quit()


if __name__ == "__main__":
    log_in()
    test()
    # acquire_cookies()
