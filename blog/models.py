import datetime

from mongoengine import *

SOURCES = (('du', 'Direct Upload'),
           ('tu', 'Tumblr Post'),
           ('tw', 'Tweet'),
           ('ig', 'Instagram'),
           ('fb', 'Facebook'))


class Photo(Document):
    image_path = StringField(required=True)
    thumbnail_path = StringField(required=True)
    width = IntField(required=True)
    height = IntField(required=True)

    def to_json(self):
        return {'image_path': self.image_path,
                'thumbnail_path': self.thumbnail_path,
                'width': self.width,
                'height': self.height}

class Post(Document):
    slug = StringField(required=True)
    title = StringField(required=True)
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
                'photos': [p.as_dict() for p in self.photos]}

        if hasattr(self, 'tags'):
            d['tags'] = self.tags
        return d

