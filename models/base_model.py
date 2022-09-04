#!/usr/bin/python3
""" base class that defines all common attributes/methods for other classes """


import uuid
from datetime import datetime
import models


class BaseModel:
    """ base class of all other classes """
    def __init__(self, *args, **kwargs):
        """ constructor function """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(value)
                elif key == '__class__':
                    continue
                else:
                    self.__dict__[key] = value

    def save(self):
        """ updates public attribute updated_at with current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ returns dictionary with keys/values of __dict__ of the instance """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()
        return new_dict

    def __str__(self):
        """ str function """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def __repr__(self):
        """ repr function """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
