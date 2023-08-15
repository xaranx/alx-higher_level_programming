#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        first = sentence[0]
    else:
        return None
    return (length, first)
