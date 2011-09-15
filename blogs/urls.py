from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'demo.blogs.views.blogs'),
    (r'^add/$', 'demo.blogs.views.add_blog'),
)
