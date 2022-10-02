#!/usr/bin/env python3
import os


def main():
    print("Hello!")
    print(os.environ.get("GITHUB_ACTION", "$GITHUB_ACTION not found"))
    print("::warning file=FILENAME,title=Warning Title::This is a warning")
    print("::error::This is an error")


if __name__ == "__main__":
    main()
