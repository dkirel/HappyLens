
from django.shortcuts import render
from django.http import HttpResponseRedirect

from acct.forms import LoginForm
from acct.models import User


def log_in(request):
    """Login page view"""
    form = LoginForm()
    invalid_login = False

    if form.is_valid():

        data = form.cleaned_data
        user = User.objects(email=data['email'])

        if user is not None and user.authenticate(password=data['password']):
            return HttpResponseRedirect('/')

    return render(request, 'acct/authenticate.html', locals())

