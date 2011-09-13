from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404


from forms import LoginForm

def login_user(request):
    state = 'Please login below ...'
    username = password = ''
    form = LoginForm()
    if not request.user.is_active:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        state = 'You are successfully logged in!'
                    else:
                        state = 'Your account is not active. Please contact site admin.'
                else:
                    state = 'Username and/or password was incorrect.'
            else:
                state = 'You didn t filled the form properly.'
        return render_to_response('auth/login.html', RequestContext(request, {'form':form, 'state':state, 'username': username}))
    else:
        return HttpResponseRedirect('/blogs')

