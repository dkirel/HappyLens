import datetime
import random
import string
import bcrypt

from mongoengine import *
from django.db import models
from django.contrib import admin
from django.conf import settings
from django_mongodb_engine.storage import GridFSStorage

gridfs_storage = GridFSStorage()

SOURCES = (('du', 'Direct Upload'),
           ('tu', 'Tumblr Post'),
           ('tw', 'Tweet'),
           ('ig', 'Instagram'),
           ('fb', 'Facebook'))

class Project(Document):
    name = StringField(required=True)
    description = StringField()

class Photo(Document):
    image_name = StringField(required=True)
    image_path = StringField(required=True)
    project = StringField(required=True)
    thumbnail_path = StringField()
    width = IntField()
    height = IntField()

    def to_json(self):
        return {
            'image_name': self.image_name,
            'image_path': self.image_path,
            'thumbnail_path': self.thumbnail_path,
            'width': self.width,
            'height': self.height
        }


class Post(Document):
    slug = StringField(required=True)
    title = StringField(required=True)
    project = StringField(required=True)
    timestamp = DateTimeField(required=True, default=datetime.datetime.now)
    photos = ListField(ReferenceField(Photo), required=True)
    tags = ListField(StringField())
    source = StringField(required=True, choices=SOURCES)
    meta = {
        'indexes': [
            {'fields': ['slug'], 'unique': True, 'types': False}
        ]
    }

    def to_json(self):
        d = {'title': self.title,
                'slug': self.slug,
                'date': self.date.strftime('%Y-%m-%d'),
                'source': self.source,
                'photos': [p.to_json() for p in self.photos]}

        if hasattr(self, 'tags'):
            d['tags'] = self.tags
        return d


