# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404


from models import Blog
from forms import BlogForm

def blogs(request):
    blogs = Blog.objects.order_by('-timestamp')
    form = BlogForm()
    return render_to_response('blogs/blog_list.html', RequestContext(request, {'blogs':blogs, 'blog_form':form}))

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect('/blogs')
        else:
            return HttpResponse('Some error occured please try again later.')

