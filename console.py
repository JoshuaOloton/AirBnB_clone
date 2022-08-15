#!/usr/bin/python3
""" entry point of command interpreter """

import cmd
from models import storage
import shlex
import re
import ast
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State


class HBNBCommand(cmd.Cmd):
    """ command interpreter """
    prompt = "(hbnb) "

    valid_classes = [
        "BaseModel", "User", "Place", "State", "City", "Amenity", "Review"
        ]
    int_attrs = [
        "number_rooms", "number_bathrooms", "max_guest", "price_by_night", "age", "my_number"
        ]
    float_attrs = [
        "latitude", "longitude"]

    # basic operational commands
    def emptyline(self):
        """ Method called when an empty line is
        entered in response to the prompt """
        pass

    def default(self, line):
        """ when command prefix is not recognized """
        if line == 'EOF':
            return True
        super().default(line)

    def do_quit(self, arg):
        """ Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program\n"""
        return True
    
    # program commands
    def do_create(self, line):
        """Create new instance of class mode\n"""
        if not line:
            print("**class name missing**")
            return False
        args = line.split()
        if args[0] == "BaseModel":
            model = BaseModel()
        elif args[0] == "User":
            model = User()
        elif args[0] == "Amenity":
            model = Amenity()
        elif args[0] == "City":
            model = City()
        elif args[0] == "Place":
            model = Place()
        elif args[0] == "Review":
            model = Review()
        elif args[0] == "State":
            model = State()
        else:
            print("** class doesn't exist **")
            return False
        print(model.id)
        model.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
