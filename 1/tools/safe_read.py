#!/usr/bin/env python3
import argparse

def main():
    ap = argparse.ArgumentParser(description="Chunked safe file reader to avoid RangeError on large files")
    ap.add_argument("path", help="Path to the file to read")
    ap.add_argument("chunk", nargs="?", type=int, default=4096, help="Chunk size in bytes (default 4096)")
    args = ap.parse_args()

    path = args.path
    chunk = max(1, int(args.chunk))
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        while True:
            data = f.read(chunk)
            if not data:
                break
            print(data, end="")

if __name__ == "__main__":
    main()
