from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = patterns(
    url(r'', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls'))
)
