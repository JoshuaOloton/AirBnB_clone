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

    def do_show(self, line):
        """Print string representation of instance\n"""
        all_objs = storage.all()
        if not line:
            print("** class name missing **")
            return False
        args = line.split()
        if args[0] not in type(self).valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] not in all_objs:
            print("** no instance found**")
        else:
            print(all_objs[args[0]+"."+args[1]]._str_())

    def do_destroy(self,line):
        """Deletes an instance based on the class name\n"""
        if not line:
            print("** class name missing **")
            return False
        args = line.split()
        if args[0] not in type(self).valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] not in storage.all():
            print("** no instance found **")
        else:
            storage.all().pop(args[0]+"."+args[1])
            storage.save()

    def do_all(self,line):
        """Prints all string representation of all instances\n"""
        all_list = []
        if line:
            args = line.split()
            if args[0] not in type(self).valid_classes:
                print("** class doesn't exist **")
                return False
            for key, value in storage.all().items():
                all_list.append(value._str_())
            print(all_list)

    def do_update(self, line):
        """  Updates an instance based on the class name and id\n"""
        if not line:
            print("** class name missing **")
            return False
        args = shlex.split(line)
        if args[0] not in type(self).valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0]+"."+args[1] not in storage.all():
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = storage.all()[args[0]+"."+args[1]]
            value = args[3]
            if args[2] == 'age' or args[2] == 'my_number':
                value = int(args[3])
            obj._dict_[args[2]] = value
            storage.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
