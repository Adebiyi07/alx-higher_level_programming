#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        # Attempt to print the integer value
        print("{:d}".format(value))
        return True
    except Exception as e:
        # Print the error message to stderr and return False
        print(f"Exception: {e}", file=sys.stderr)
        return False
