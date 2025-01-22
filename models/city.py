#!/usr/bin/python3
"""This is the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This class represents a City"""

    def __init__(self, *args, **kwargs):
        """Initialize a City instance"""
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get("state_id", "")
        self.name = kwargs.get("name", "")