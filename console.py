#!/usr/bin/python3
""" entry point of command interpreter """

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ command interpreter """
    prompt = "(hbnb) "

    valid_classes = ["BaseModel"]

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
        """ Create new instance of class model\n"""
        if not line:
            print("** class name missing **")
            return False
        args = line.split()
        if args[0] == "BaseModel":
            base_model = BaseModel()
            print(base_model.id)
            base_model.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """ Print string representation of instance\n"""
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
            print("** no instance found **")
        else:
            print(all_objs[args[0]+"."+args[1]].__str__())

    def do_destroy(self, line):
        """ Deletes an instance based on the class name\n"""
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

    def do_all(self, line):
        """ Prints all string representation of all instances\n"""
        all_list = []
        args = line.split()
        if args[0] not in type(self).valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                all_list.append(value.__str__())
            print(all_list)

    def do_update(self, line):
        """  Updates an instance based on the class name and id\n"""
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
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj = storage.all()[args[0]+"."+args[1]]
            value = args[3]
            if args[2] == 'age' or args[2] == 'my_number':
                value = int(args[3])
            obj.__dict__[args[2]] = value


if __name__ == "__main__":
    HBNBCommand().cmdloop()
