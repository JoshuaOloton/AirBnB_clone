#!/usr/bin/python3
""" entry point of command interpreter """

import cmd
from models import storage


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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
