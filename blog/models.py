import datetime
import random
import string
import bcrypt
import os

from django.db import models
from django.conf import settings
from django.contrib import admin
from django import forms
from djangotoolbox.fields import EmbeddedModelField, ListField

SOURCES = (('du', 'Direct Upload'),
           ('tu', 'Tumblr Post'),
           ('tw', 'Tweet'),
           ('ig', 'Instagram'),
           ('fb', 'Facebook'))

def get_image_path(self, other_field):
    return 'uploads/' + self.project.replace(' ', '_').lower() + '/' + os.path.basename(self.image_name)

class Profile(models.Model):
    name = models.CharField(blank=False, max_length=100)
    photo = models.ImageField(blank=False, max_length=50)
    personal_info = models.CharField(blank=False, max_length=1000)

    def __unicode__(self):
       return self.name

class ProfileForm(forms.ModelForm):
    personal_info = forms.CharField(required=True, widget=forms.Textarea, max_length=1000)
    class Meta:
        model = Profile

class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm


class Project(models.Model):
    name = models.CharField(blank=False, max_length=100)
    description = models.CharField(blank=True, max_length=500)

    def __unicode__(self):
       return self.name

class ProjectForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea, max_length=1000)
    class Meta:
        model = Project

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm


class Photo(models.Model):
    image_name = models.CharField(blank=False, max_length=300)
    project = models.CharField(blank=False, choices=((p.name, p.name) for p in Project.objects.all()), max_length=100)
    file = models.ImageField(blank=False, upload_to=get_image_path)
    thumbnail_path = models.CharField(max_length=500, editable=False)
    project_cover = models.BooleanField()

    def __unicode__(self):
       return self.project + '/' + self.image_name

    def to_json(self):
        return {
            'image_name': self.image_name,
            'image_path': self.image_path,
            'thumbnail_path': self.thumbnail_path,
            'width': self.width,
            'height': self.height
        }

"""
class Post(models.Model):
    slug = models.CharField(blank=False, max_length=200)
    title = models.CharField(blank=False, max_length=200)
    project = models.CharField(blank=False, max_length=200)
    timestamp = models.DateTimeField(blank=False, default=datetime.datetime.now)
    photos = EmbeddedModelField('Photo', blank=False)
    tags = ListField(models.CharField())
    source = models.CharField(blank=False, choices=SOURCES, max_length=50)
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
"""

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Photo)

