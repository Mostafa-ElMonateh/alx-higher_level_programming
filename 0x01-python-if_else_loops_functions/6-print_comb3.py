#!/usr/bin/python3
for lDigit in range(0, 10):
    for rDigit in range(lDigit + 1, 10):
        if lDigit == 8 and rDigit == 9:
            print("{}{}".format(lDigit, rDigit))
        else:
            print("{}{}".foramt(lDigit, rDigit), end=", ")
