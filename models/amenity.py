#!/usr/bin/python3
"""Defines the amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    child class of BaseModel
    has one attribute - name(empty string)
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
