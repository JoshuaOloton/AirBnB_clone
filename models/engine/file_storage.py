#!/usr/bin/python3
""" FileStorage class that serializes instances to a JSON
file and deserializes JSON file to instances """

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.user import User


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
        type(self).__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        json_ret = {}
        for key, value in type(self).__objects.items():
            json_ret[key] = value.to_dict()
        with open(type(self).__file_path, 'w', encoding='utf-8') as file:
            json.dump(json_ret, file)

    def reload(self):
        """ deserializes JSON file to __objects (if (__file_path) exists """
        try:
            with open(type(self).__file_path, encoding='utf-8') as file:
                loaded_dict = json.load(file)
        except Exception:
            return
        else:
            from models import base_model
            for key, value in loaded_dict.items():
                obj_class = eval(value["__class__"])
                # type(self).__objects[key] = obj_class(**value)
                del o["__class__"]
                self.new(obj_class(**value))
