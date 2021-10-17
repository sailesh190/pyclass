import unittest
from hierarchical_json import search_cat_info, process_list

supposed_input = [
    {
        "id": 2,
        "name": "cat2",
        "parent_id": 1,
        "path_info": [1, 2]
    },
    {
        "id": 1,
        "name": "cat1",
        "parent_id": None,
        "path_info": [1]
    }
]

desired_search_output_1 = None

desired_search_output_2 = {
    "id": 2,
    "name": "cat2",
    "parent_id": 1,
}

desired_process_output = [
    {
        'id': 2,
        'name': 'cat2',
        'parent_id': 1,
        'subcats': [
            {
                'id': 2,
                'name': 'cat2',
                'parent_id': 1
            }
        ]
    },
    {
        'id': 1,
        'name': 'cat1',
        'parent_id': None,
        'subcats': []
    }
]

class TestHierarchicalJson(unittest.TestCase):

    def test_search_1(self):
        self.assertEqual(search_cat_info(1, supposed_input), desired_search_output_1)

    def test_search_2(self):
        self.assertEqual(search_cat_info(2, supposed_input), desired_search_output_2)

    def test_process(self):
        self.assertEqual(process_list(supposed_input), desired_process_output)

if __name__ == "__main__":

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
