#!/usr/bin/python3
def raise_exception():
    try:

        result = "string" + 123
    except TypeError as e:

        raise e
