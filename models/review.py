#!/usr/bin/python3
"""This is the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class represents a Review"""

    def __init__(self, *args, **kwargs):
        """Initialize a Review instance"""
        super().__init__(*args, **kwargs)
        self.place_id = kwargs.get("place_id", "")
        self.user_id = kwargs.get("user_id", "")
        self.text = kwargs.get("text", "")