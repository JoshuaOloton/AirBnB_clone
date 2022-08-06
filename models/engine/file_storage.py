#!/usr/bin/python3
""" FileStorage class that serializes instances to a JSON
file and deserializes JSON file to instances """

import json

class FileStorage:
    """ File Storage class inherits from BaseModel class """
    __file_path = "file.json"
    __objects = {}

    #@staticmethod
    def all(self):
        """ returns the dictionary __objects """
        return type(self).__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        type(self).__objects[key] = obj.to_dict()

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(type(self).__file_path, 'w', encoding='utf-8') as file:
            json.dump(type(self).__objects, file)

    def reload(self):
        """ deserializes the JSON file to __objects (if (__file_path) exists """
        try:
            with open(type(self).__file_path, encoding='utf-8') as file:
                type(self).__objects = json.load(file)
        except:
            pass
