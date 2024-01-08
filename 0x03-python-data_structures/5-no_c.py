#!/usr/bin/bash
def no_c(my_string):
    newString = ''
    for char in my_string:
        if char.lower() not in {'c', 'C'}:
            newString += char
    return newString
