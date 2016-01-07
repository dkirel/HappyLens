from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import index

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^acct/', include('acct.urls')),
    url(r'^blog/', include('blog.urls'))
)
