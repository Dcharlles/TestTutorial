def revert_string(string: str):
    try:
        return string[::-1]
    except TypeError:
        return None

def append_elements_to_array(array, *elements):
    return [*array, *elements]

def calculate_string_operation(operation: str):
    try:
        return eval(operation)
    except Exception:
        return None

def copy_dict(dictionary: dict):
    return {
        **dictionary
    }