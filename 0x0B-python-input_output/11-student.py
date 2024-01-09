#!/usr/bin/python3
"""This file contains the 'Student' class definition
"""


class Student:
    """
    A class to represent a student.

    Attributes
    ----------
    first_name : str
        The first name of the student
    last_name: str
        The last name of the student
    age : int
        The age of the student.

    Methods
    -------
    __init__(name, age)
        Constructor method to initialize the dog with a name and age.
    to_json()
        retrieves a dictionary representation of a Student instance
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=['first_name', 'last_name', 'age']):
        new_dic = vars(self)
        return {x: new_dic[x] for x in attrs if x in list(new_dic.keys())}

    def reload_from_json(self, json):
        for k, v in json.items():
            setattr(self, k, v)
