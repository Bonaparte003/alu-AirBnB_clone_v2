#!/usr/bin/python3
"""File storage system for objects instead of SQLAlchemy"""
import json
from os import getenv
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Class that serializes and deserializes instances to and from a JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of all objects, or objects of a specific class"""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = value["__class__"]
                    self.__objects[key] = eval(cls_name)(**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it exists"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in self.__objects:
                del self.__objects[key]
                self.save()

    def close(self):
        """Closes the storage session (for compatibility with SQLAlchemy-based code)"""
        self.reload()