
def set_dict_value(dictionary, key, value) -> None:
    """
    Set a value in a dictionary, adding to it if the key already exists.
    """
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value
        
def set_dict_value_list(dictionary, key, value) -> None:
    """
    Set a value in a dictionary, adding to it if the key already exists.
    """
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]