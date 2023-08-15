#!/usr/bin/python3
"""module documentation"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """The Basemodel for hbnb"""
    def __init__(self, *args, **kwargs):
        """initializes the class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """string output representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}>"

    def save(self):
        """saves the instance of the class"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        n_dict = self.__dict__.copy()
        n_dict["__class__"] = self.__class__.__name__
        if "created_at" in n_dict:
            n_dict["created_at"] = n_dict["created_at"].isoformat()
        if "updated_at" in n_dict:
            n_dict["updated_at"] = n_dict["updated_at"].isoformat()
        return n_dict
