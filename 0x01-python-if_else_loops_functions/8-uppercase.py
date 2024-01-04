#!/usr/bin/python3
def uppercase(str):
    for j in str:
        lower = j
        if ord(lower) >= 97 and ord(lower) <= 122:
            lower = chr(ord(j) - 32)
        print("{}".format(lower), end='')
    print()
