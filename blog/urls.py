from django.conf.urls import url

from . import views


urlpatterns = [
    #Browse projects
    url(r'index$', views.home, name='home'),
    url(r'project/(?P<project>[\w|\W]+)$', views.browse_project, name='browse-project'),

    #Post admin
    url(r'^post-photo$', views.post_photo, name='post-photo')

]
