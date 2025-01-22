#!/usr/bin/python3
"""This is the file storage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and deserializes back"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves objects to JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Loads objects from JSON file"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = value["__class__"]
                    self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            pass