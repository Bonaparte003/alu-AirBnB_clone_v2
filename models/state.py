#!/usr/bin/python3
"""This is the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class represents a State"""

    def __init__(self, *args, **kwargs):
        """Initialize a State instance"""
        super().__init__(*args, **kwargs)
        self.name = kwargs.get("name", "")