from django.conf.urls import url

from . import views


urlpatterns = [
    #Browse projects
    url(r'^$', views.home, name='home'),
    url(r'project/(?P<project>[\w|\W]+)$', views.browse_project, name='browse-project'),
    url(r'about$', views.about, name='about'),
    url(r'contact$', views.contact, name='contact')

    #Post admin
    #url(r'^post-photo$', views.post_photo, name='post-photo')

]
