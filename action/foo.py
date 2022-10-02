#!/usr/bin/env python3
import os


def main():
    print("Hello world!")
    print(os.environ.get("GITHUB_ACTION", "$GITHUB_ACTION not found"))
    print("::notice file=app.js,line=1,col=5,endColumn=7::Missing semicolon")
    print("::warning file=app.js,line=1,endLine=5,title=TITLE::MESSAGE")
    print("::warning file=FILENAME,title=Warning Title::This is a warning")
    print("::error::This is an error")


if __name__ == "__main__":
    main()
