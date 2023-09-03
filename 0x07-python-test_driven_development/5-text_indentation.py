#!/usr/bin/python3


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")
