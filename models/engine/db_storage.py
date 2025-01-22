from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv
from models.base_model import Base

class DBStorage:
    """ Database storage engine """

    __engine = None
    __session = None

    def __init__(self):
        """ Initialize the storage system """
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query all objects based on class """
        obj_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = f"{obj.__class__.__name__}.{obj.id}"
                obj_dict[key] = obj
        else:
            from models.user import User
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.place import Place
            from models.review import Review

            classes = [User, State, City, Amenity, Place, Review]
            for cls in classes:
                objs = self.__session.query(cls).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """ Add the object to the session """
        self.__session.add(obj)

    def save(self):
        """ Commit the changes to the database """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete an object from the session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Load all tables and create a session """
        from models.base_model import Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()