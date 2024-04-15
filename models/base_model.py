#!/usr/bin/python3

import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """class from which other classes inherit"""
    def __init__(self, *args, **kwargs):
        "nitializes instance attributes

        *args: list of arguments
        
        **kwargs: a dictionary of key-values arguments
    """
        if kwargs not None and kwargs !={}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.created_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns the official string representation"""
        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)
    def save(self):
        """updates the public instance attribute updated_at"""
        self updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary with all keys/values of __dict_"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
