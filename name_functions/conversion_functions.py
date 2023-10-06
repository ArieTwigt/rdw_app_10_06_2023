from typing import List

def capitalize_names(names_list: List[str]) -> List[str]:
    """
    Functions that returns a list with names capitalized

    Input:
    * names_list: list with names

    Output:
    * new_names list: list with capitalized names
    
    """
    
    # define the new names list
    new_names_list = []

    # iterate over thte names
    for name in names_list:
        new_names_list.append(name.capitalize())

    # or as a list
    new_names_list = [name.capitalize() for name in names_list]

    return new_names_list