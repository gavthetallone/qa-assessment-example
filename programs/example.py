    # <QUESTION 1>

    # Given a string, return the boolean True if it ends in "py", and False if not. Ignore Case.

    # <EXAMPLES>

    # endsPy("ilovepy") → True
    # endsPy("welovepy") → True
    # endsPy("welovepyforreal") → False
    # endsPy("pyiscool") → False

    # <HINT>

    # What was the name of the function we have seen which changes the case of a string?  Use your CLI to access the Python documentation and get help(str).
    
def endsPy(input):
    py_str = input

    if py_str[-2] == "p" and py_str[-1] == "y":
        return True
    elif py_str[-2] == "p" and py_str[-1] == "Y":
        return True
    elif py_str[-2] == "P" and py_str[-1] == "y":
        return True
    elif py_str[-2] == "P" and py_str[-1] == "Y":
        return True
    else:
        return False
    