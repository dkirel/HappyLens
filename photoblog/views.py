from django.http import HttpResponseRedirect
from django.shortcuts import redirect

def index(request):
    return redirect('/blog')



