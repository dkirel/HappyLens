from mongoengine import *

from models import User

connect('happy_lens')

email = raw_input('Email: ')
username = raw_input('Username: ')
password = getpass.getpass()

admin = User(username=username, email=email, password=password)
print 'Successfully created admin user {username}!'

