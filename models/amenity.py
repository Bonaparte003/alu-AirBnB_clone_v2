#!/usr/bin/python3
"""This is the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """This class represents an Amenity"""

    def __init__(self, *args, **kwargs):
        """Initialize an Amenity instance"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name", "")