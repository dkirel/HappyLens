from django import forms
from django_mongodb_engine.storage import GridFSStorage
from mongoengine import connect

from .models import Project

connect('happy_lens', host='mongodb://happy_lens:happylens9@ds049854.mongolab.com:49854/happy_lens')
gridfs_storage = GridFSStorage()

class ProjectForm(forms.Form):
    project_name = forms.CharField(label="Project Name", required=True)


class PostForm(forms.Form):

    slug = forms.CharField(required=True)
    title = forms.CharField(required=True)
    project = forms.ChoiceField(choices=(("Street Fashion", "Street Fashion"), ("Exhibit Muses", "Exhibit Muses"), ("Green Muses", "Green Muses")), required=True)
    files = forms.ImageField(required=True)




