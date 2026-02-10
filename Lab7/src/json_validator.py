"""
JSON Structure Validator — Lab 7

Validates the structural nesting of a JSON string using a Stack.
Reports the location (line, column) of any errors found.
"""

from stack import Stack


# Maps each closing character to its expected opening character.
MATCHING = {
    "}": "{",
    "]": "[",
}


def validate(json_string):
    """
    Validate the structural nesting of a JSON string.

    Checks that every { has a matching }, every [ has a matching ],
    and that quoted strings are properly closed.

    Args:
        json_string (str): The JSON text to validate.

    Returns:
        tuple: (is_valid, errors)
            - is_valid (bool): True if the structure is valid.
            - errors (list[str]): List of error message strings.
              Empty if valid.
    """
    Valid = Stack()
    line = 1
    column = 0
    in_string == False
    for char in json_string:
        if char == "\n":
            line += 1
            column = 0
        if in_string == True:
            if char == '\\':
                char += 1
            elif char == '"':
                SET in_string = False
        if char == '"':
            SET in_string == True
        if char == '{' or char == "[":
            Valid.push(char,line,column)
        elif char == '}' or char == ']':
            if Valid.is_empty() == True:
                REPORT error: "Unexpected closer at (" + line + ", " + column + ")"
                return "Failure"
            open_char,open_line,open_col = Valid.pop()
            if open_char != char:
                REPORT error: "expected matching closer for "+ open_char+" at ("+ open_line+", " + open_col +") but found " + char + "at (" + line + ", " + column +")"
                return "failure"
        if in_string == True:
            REPORT error: "untermindated string"
            return "failure"
        if Valid.is_empty() == False:
            for num in Valid.size():
                open_char,open_line,open_col = Valid.pop()
                REPORT error: "Unclosed " + open_char+" at ("+open_line+", "+open_col+")"
            return "Failure"
        return "Success"



        




def validate_file(filepath):
    """
    Validate a JSON file by reading it and calling validate().

    Args:
        filepath (str): Path to the JSON file.

    Returns:
        tuple: (is_valid, errors) — same as validate().
    """
    with open(filepath, "r") as f:
        content = f.read()
    return validate(content)


# ── Main ─────────────────────────────────────────────────────────
# You can use this to test your validator from the command line:
#   python src/json_validator.py tests/test_data/easy_correct.json

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python json_validator.py <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]
    is_valid, errors = validate_file(filepath)

    if is_valid:
        print(f"{filepath}: Valid JSON structure")
    else:
        for error in errors:
            print(error)