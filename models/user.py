#!/usr/bin/python3
"""Defines the user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Child class of BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
