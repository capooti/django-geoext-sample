import os
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # admin url
    (r'^admin/', include(admin.site.urls)),
    
    # evaluations url
    (r'^evaluations/', include('evaluations.urls')),
    
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(__file__), "media"),
             'show_indexes': True
            }),
    )
