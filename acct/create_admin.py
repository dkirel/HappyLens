from mongoengine import *

from photoblog.blog.models import Project

connect('happy_lens', host='mongodb://dk2459:hhopolo9@ds049854.mongolab.com:49854/happy_lens')

project_name = raw_input('Project Name: ')
project = Project(name=project_name)

print('Successfully created admin user {project_name}!'.format(project_name=project_name))

