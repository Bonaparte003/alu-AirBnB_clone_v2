from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv

class State(BaseModel, Base):
    """ Represents a state """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """ Getter for cities related to the state """
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]