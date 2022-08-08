#!/usr/bin/python3
""" FileStorage class that serializes instances to a JSON
file and deserializes JSON file to instances """

import json


class FileStorage:
    """ File Storage class inherits from BaseModel class """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return type(self).__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        json_ret = {}
        for key, value in type(self).__objects.items():
            json_ret[key] = value.to_dict()
        with open(type(self).__file_path, 'w', encoding='utf-8') as file:
            json.dump(json_ret, file)

    def reload(self):
        """ deserializes JSON file to __objects (if (__file_path) exists """
        loaded_dict = {}
        try:
            with open(type(self).__file_path, encoding='utf-8') as file:
                loaded_dict = json.load(file)
        except Exception:
            pass
        from models import base_model
        for key, value in loaded_dict.items():
            type(self).__objects[key] = base_model.BaseModel(**value)
