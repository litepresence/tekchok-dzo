def letter_to_number(letter: str) -> int:
    letter = letter.upper()
    if not letter.isalpha() or len(letter) != 1:
        raise ValueError(f"Letter part must be a single alphabetic character, got {letter}")
    return ord(letter) - ord('A') + 1


def roman_to_int(roman: str) -> int:
    roman = roman.upper()
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    total = 0
    prev = 0
    for char in reversed(roman):
        if char not in values:
            raise ValueError(f"Invalid Roman numeral character: {char}")
        curr = values[char]
        if curr < prev:
            total -= curr
        else:
            total += curr
            prev = curr

    return total


def parse_roman(s: str) -> str:
    try:
        letter_part, roman_part = s.split("-")
    except ValueError:
        try:
            return letter_to_number(s)
        except:
            raise ValueError("Input must be in the form LETTER-ROMAN or LETTER")

    letter_num = letter_to_number(letter_part)
    roman_num = roman_to_int(roman_part)

    return f"{letter_num}_{roman_num}"


if __name__ == '__main__':
    print(parse_value("C-iv"))   # 3-4
    print(parse_value("A-XII"))  # 1-12
