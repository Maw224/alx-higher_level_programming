#!/usr/bin/python3

def multiple_returns(sen):
    if len(sen) == 0:
        return 0, None
    return len(sen), sen[0]
