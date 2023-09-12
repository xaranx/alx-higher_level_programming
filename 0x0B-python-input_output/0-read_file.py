#!/usr/bin/python3

def read_file(filename=""):
    """
    Methode for Read line
    """
    with open("my_file_0.txt", encoding="utf-8") as f:
        print(f.read(), end="")
