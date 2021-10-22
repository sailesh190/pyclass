#-*- coding  = utf-8 -*-
#@Time : 10/13/21 7:14 PM
#@Author : Malumolo
#@ File: pytest.py
#@Software: PyCharm

# pytest --cov=ops . -v --cov-report term-missing 

"""
create hirerachical json dump from list of dict

A category can have many children, but only 1 parent. I have got the list of dictionary values as follows using CTE:
 eg. For id :14, parent is 13 and traversed from parent 8->10->12->13->14 where parent 8 has no parent id.

Notice that 'path_info' has been deleted from the dictionary and each id has been displayed with its details.
Input:
  {
      "array": [
          {
            "id": 14,
            "name": "cat14",
            "parent_id": 13,
            "path_info": [
              8,
              10,
              12,
              13,
              14
            ]
          },
          {
            "id": 15,
            "name": "cat15",
            "parent_id": 13,
            "path_info": [
              8,
              10,
              12,
              13,
              15
            ]
          },
          {
            "id": 13,
            "name": "cat13",
            "parent_id": 12,
            "path_info": [
              8,
              10,
              12,
              13
            ]
          },
         {
            "id": 12,
            "name": "cat12",
            "parent_id": 10,
            "path_info": [
              8,
              10,
              12
            ]
          },
          {
            "id": 10,
            "name": "cat10",
            "parent_id": 8,
            "path_info": [
              8,
              10
            ]
          },
          {
            "id": 8,
            "name": "cat8",
            "parent_id": null,
            "path_info": [
              8
            ]
          }
        ]
    }

Output:
 [
     {
      "name": "cat14",
      "subcats": [
       {
        "name": "cat10",
        "id": 10,
        "parent_id": 8
       },
       {
        "name": "cat12",
        "id": 12,
        "parent_id": 10
       },
       {
        "name": "cat13",
        "id": 13,
        "parent_id": 12
       },
       {
        "name": "cat14",
        "id": 14,
        "parent_id": 13
       }
      ],
      "id": 14,
      "parent_id": 13
     },
     {
      "name": "cat15",
      "subcats": [
       {
        "name": "cat10",
        "id": 10,
        "parent_id": 8
       },
       {
        "name": "cat12",
        "id": 12,
        "parent_id": 10
       },
       {
        "name": "cat13",
        "id": 13,
        "parent_id": 12
       },
       {
        "name": "cat15",
        "id": 15,
        "parent_id": 13
       }
      ],
      "id": 15,
      "parent_id": 13
     },
     {
      "name": "cat13",
      "subcats": [
       {
        "name": "cat10",
        "id": 10,
        "parent_id": 8
       },
       {
        "name": "cat12",
        "id": 12,
        "parent_id": 10
       },
       {
        "name": "cat13",
        "id": 13,
        "parent_id": 12
       }
      ],
      "id": 13,
      "parent_id": 12
     },
     {
      "name": "cat12",
      "subcats": [
       {
        "name": "cat10",
        "id": 10,
        "parent_id": 8
       },
       {
        "name": "cat12",
        "id": 12,
        "parent_id": 10
       }
      ],
      "id": 12,
      "parent_id": 10
     },
     {
      "name": "cat10",
      "subcats": [
       {
        "name": "cat10",
        "id": 10,
        "parent_id": 8
       }
      ],
      "id": 10,
      "parent_id": 8
     },
     {
      "name": "cat8",
      "subcats": [],
      "id": 8,
      "parent_id": null
     }
    ]

1) Write the logic
2) Use docstrings
3) Make sure , your pylint is score 10
4) All test case should pass
5) You need ad coverage report.
"""