#!/usr/bin/python3
"""Program to check if object is an instance of a class
or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Return true if object is an instance of a class,
	if the object is an instance of a class that inherited from
    """
    return (isinstance(obj, a_class))
