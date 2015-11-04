import random
import string

import bcrypt
from mongoengine import *

class User(Document):
    email = EmailField(required=True, unique=True)
    username = StringField(required=True, primary_key=True)
    password = StringField(required=True)
    auth = StringField(required=True, default=''.join(random.choice(string.hexdigits) for i in range(32)))

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        if len(password) < 6:
            raise ValueError("Password must be at least 6 characters long")

        self.password = bcrypt.hashpw(password, bcrypt.gensalt())
        self.save()

    def authenticate(self, password=None, auth=None):
        if auth and auth == self.auth:
            return True
        if not password:
            raise ValueError("Password or auth required")

        return bcrypt.hashpw(password, hashed) == hashed
