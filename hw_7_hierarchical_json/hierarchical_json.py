"""
Assignment:
create hirerachical json dump from list of dict
A category can have many children, but only 1 parent. I have got the
list of dictionary values as follows using CTE:
eg. For id :14, parent is 13 and traversed from parent
8->10->12->13->14 where parent 8 has no parent id.
Notice that 'path_info' has been deleted from the dictionary and each
id has been displayed with its details.
1) Write the logic
2) Use docstrings
3) Make sure , your pylint is score 10
4) All test case should pass
5) You need ad coverage report.

Solution:
Each id number in the path_info of each element which is a dictionary
is used to fetch the category information from the given list.
The information is then appended to the "subcats" item of the dictionary.
The "path_info" item is then removed from the dictionary.
"""

import json
import copy

def search_cat_info(id_number, list_to_process):

    """
    This function searches the category information from list_to_process
    with id_number.
    param id_number: int
    param list_to_process: a list of dictionaries
    return: dictionary
    """

    for item in list_to_process:

        if item["id"] == id_number and item["parent_id"] is not None:

            item_copied = item.copy()

            item_copied.pop('path_info')

            return item_copied

    return None

def process_list(list_to_process):

    """
    For each dictionary of list_to_process, this function removes
    "path_info" and append the category information of each element
    in "path_info" to the item "subcats".
    param list_to_process: a list of dictionaries
    return: a list of dictionaries
    """
    copied_list = copy.deepcopy(list_to_process)

    for item in copied_list:

        path_info = item.pop("path_info")

        subcats = []

        for id_number in path_info:

            subcat = search_cat_info(id_number, list_to_process)

            if subcat is not None:

                subcats.append(subcat)

        item["subcats"] = subcats

    return copied_list

if __name__ == "__main__":

    JSON_INPUT = """
    {
        "array": [
            {
                "id": 14,
                "name": "cat14",
                "parent_id": 13,
                "path_info": [8, 10, 12, 13, 14]
            },
            {
                "id": 15,
                "name": "cat15",
                "parent_id": 13,
                "path_info": [8, 10, 12, 13, 15]
            },
            {
                "id": 13,
                "name": "cat13",
                "parent_id": 12,
                "path_info": [8, 10, 12, 13]
            },
            {
                "id": 12,
                "name": "cat12",
                "parent_id": 10,
                "path_info": [8, 10, 12]
            },
            {
                "id": 10,
                "name": "cat10",
                "parent_id": 8,
                "path_info": [8, 10]
            },
            {
                "id": 8,
                "name": "cat8",
                "parent_id": null,
                "path_info": [8]
            }
        ]
    }
    """

    LIST_INPUT = json.loads(JSON_INPUT)["array"]

    LIST_OUTPUT = process_list(LIST_INPUT)

    JSON_OUTPUT = json.dumps(LIST_OUTPUT)

    print(JSON_OUTPUT)
