#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    '''
    This is the base model that takes care of
    the initialization, serialization and dese
    rialization of your future instances

    Attributes:
        - id(str): This is an UUID for when an        instance is created
        - created_at(datetime): This will assi
        gn  instance with date & time it was
        created
        - updated_at(datetime): This will assi
        gn instance with date & time it was up
        dated
    '''

    def __init__(self, *args, **kwargs):
        '''
        initializes attributes: id, created_at,
        updated_at
        '''

        dateformat = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "__class__" == key:
                    continue
                if "created_at" == key:
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], dateformat)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(
                        kwargs["updated_at"], dateformat)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
