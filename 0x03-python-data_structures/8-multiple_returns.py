#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, None)  # Empty sentence case
    else:
        return (len(sentence), sentence[0])  # Non-empty sentence case
