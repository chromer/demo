from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^login/$', 'demo.auth.views.login_user'),
                       )
