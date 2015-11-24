import os
import string

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from django.conf import settings
from .forms import ProjectForm, PostForm
from blog.models import Project, Post, Photo
from .publish import *


def home(request):
    """Landing page of the blog which allows users to browse projects"""

    projects = Project.objects().order_by('name')
    photos = []

    for p in projects:
        pic = Photo.objects(project=p.name).first()
        photos.append(pic)

    return render(request, 'blog/home_slideshow.html', locals())


def browse_project(request, project):
    """Photo browsing page of a particular project"""

    projects = Project.objects().order_by('name')
    photos = Photo.objects(project=project)

    return render(request, 'blog/project_slideshow.html', locals())


def post_photo(request):
    """Area to post a photo"""

    project_form = ProjectForm()
    post_form = PostForm()


    if request.method == 'POST':

        project_form = ProjectForm(request.POST)
        post_form = PostForm(request.POST, request.FILES)

        if 'project_name' in project_form.data.keys():

            if project_form.is_valid():

                #Create project doc
                data = project_form.cleaned_data
                project = Project(data['project_name'])
                project.save()

                #Add folder if it does not already exist
                dir_path = '/media/uploads/' + data['project_name'].replace(' ', '_').lower()
                project_message = '{project_name} was added succesfully!'.format(project_name=data['project_name'])

                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)

            else:
                project_message = 'Error adding new project...'

            post_form = PostForm()

        else:

            if post_form.is_valid():

                data = post_form.cleaned_data
                file = request.FILES['files']

                image_path = '/media/uploads/' + data['project'].replace(' ', '_').lower() + '/' + os.path.basename(file.name)
                save_file(file, image_path)

                photo = Photo(
                    image_name = os.path.basename(file.name),
                    image_path = image_path,
                    project = data['project']
                    #thumbnail_path = StringField()
                )

                photo.save()

                post = Post(
                    slug = data['slug'],
                    title = data['title'],
                    project = data['project'],
                    photos = (photo.to_json(),),
                    source = 'du'
                )

                post.save()

            else:
                post_message = 'Error loading post...'

            project_form = ProjectForm()

    return render(request, 'blog/post_photo.html', locals())

