#!/usr/bin/python3
"""Module Documentation for our Airbnb Console"""
import cmd
import re
import shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curlies = re.search(r"\{(.*?)\}", arg)
    sq_brackets = re.search(r"\[(.*?)\]", arg)

    if curlies is None:
        if sq_brackets is None:
            for token in split(arg):
                return token.strip(",")
        else:
            b4_brackets = split(arg[:sq_brackets.span()[0]])
            b4_brackets1 = [token.strip(",") for token in b4_brackets]
            b4_brackets1.append(sq_brackets.group())
            return b4_brackets1
    else:
        b4_brackets = split(arg[:curlies.span()[0]])
        b4_brackets1 = [token.strip(",") for token in b4_brackets]
        b4_brackets1.append(curlies.group())
        return b4_brackets1


class HBNBCommand(cmd.Cmd):
    """Defines our Airbnb Console"""
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Does not execute anything when the line is empty"""
        pass

    def do_quit(self, arg):
        """Exit/Quits the console when executed"""
        return True

    def do_EOF(self, arg):
        """EOF signals the exit of the program/"""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new class instance and prints its id"""
        arg_1 = parse(arg)
        if len(arg_1) == 0:
            print("** class name missing **")
        elif arg_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_1[0])().id)
            storage.save()












































