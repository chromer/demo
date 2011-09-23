from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^demo/', include('demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^auth/', include('demo.auth.urls')),
    (r'^$', redirect_to, {'url':'/auth/login'}),
    (r'^blogs/', include('demo.blogs.urls')),
    (r'^logout/$', 'demo.auth.views.logout'),
    (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
