"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt: str) -> int:
    # Your code here
    # check to make sure that `txt` makes sense as an integer
    # take the string input and convert it to an integer
    # the `int` function does this for us in Python
    # call the `int` funcion, passing it the `txt` input
    
    if txt.isnumeric() is True:
        converted_int = int(txt)
        # return the converted result
        return converted_int
    else:
        return "not a valid number"

print(string_int("77"))