"""
Login and logout views for the browsable API.

Add these to your root URLconf if you're using the browsable API and
your API requires authentication.

The urls must be namespaced as 'rest_framework', and you should make sure
your authentication settings include `SessionAuthentication`.

    urlpatterns = patterns('',
        ...
        url(r'^auth', include('rest_framework.urls', namespace='rest_framework'))
    )
"""
from __future__ import unicode_literals
from django.conf.urls import patterns, url

template_name = {'template_name': 'rest_framework/login.html'}

urlpatterns = patterns('',
    
    url(r'^file/(?P<module>[a-z\.]+)/(?P<model>[A-Za-z_]*)/(?P<base_dn>.*)/(?P<pk>[A-Za-z]*)/(?P<attr>[A-Za-z]*)', 'ldapdb.views.file', name='ldapdb-file'),

)
