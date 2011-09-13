# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Blog

def blogs(request):
    blogs = Blog.objects.order_by('-timestamp')
    return render_to_response('blogs/blog_list.html', RequestContext(request, {'blogs':blogs,}))

