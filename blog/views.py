import os
import string

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, mail_admins, BadHeaderError
from django.contrib import messages
from django.contrib.auth.models import User
from django.template import RequestContext

from blog.forms import ContactForm
from blog.models import Profile, Project, Photo
from blog.forms import ContactForm


def home(request):
    """Landing page of the blog which allows users to browse projects"""

    projects = Project.objects.all().order_by('name')
    photos = []

    for p in projects:
        pics = Photo.objects.filter(project=p.name).order_by('-project_cover', 'image_name')
        photos.append(pics[0])

    return render(request, 'blog/home_slideshow.html', locals())


def browse_project(request, project):
    """Photo browsing page of a particular project"""

    projects = Project.objects.all().order_by('name')
    photos = Photo.objects.filter(project=project)

    return render(request, 'blog/project_slideshow.html', locals())


def about(request):
    """Page containing the admin profile info"""

    projects = Project.objects.all().order_by('name')
    profiles = Profile.objects.all().order_by('name')

    return render(request, 'blog/about.html', locals())

def contact(request):
    """Page containing a contact form for visitors trying to contact admins"""

    projects = Project.objects.all().order_by('name')

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            subject = [subject, "No Subject"][subject == ""]
            final_message = "Sender's name: {name}\nSender's email: {from_email}\nSubject: {subject}\n\n\nMessage:\n\n{message}\n\n".format(**locals())

            try:
                mail_admins("Contact form request", final_message)
                messages.success(request, "Your message was sent successfully! We'll get back to you as soon as we get the chance.")
                form = ContactForm()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return render(request, "blog/contact.html", locals(), context_instance=RequestContext(request))


"""
def post_photo(request):

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

"""
