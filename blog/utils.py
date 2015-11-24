from django.core.urlresolvers import reverse 
from urllib import parse

def custom_redirect(url_name, *args, **kwargs):
"""Redirects to a url with parameters"""

    url = reverse(url_name, args = args)
    params = urllib.urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)

