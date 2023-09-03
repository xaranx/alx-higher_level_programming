#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    res = ""

    in_space = True
    for char in text:
        if char in [".", "?", ":"]:
            res += char + "\n\n"
            in_space = True
        elif char == " ":
            if in_space:
                continue
        else:
            res += char
            in_space = False
    print(res.strip())
