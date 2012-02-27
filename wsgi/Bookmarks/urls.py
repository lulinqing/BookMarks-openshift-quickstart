import os.path
from django.conf.urls.defaults import patterns, include, url
from bookmarks.views import *
#from django.views.generic.simple import direct_to_template
from django.contrib.auth.views import password_change, password_change_done, logout_then_login

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^tag/([^\s]+)/$', tag_page),
    (r'^tag/$', tag_cloud_page),
    (r'^search/$', search_page),
    (r'^popular/$', popular_page),
    (r'^bookmark/(\d+)/$', bookmark_page),

    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^logout_then_login/$', logout_then_login),
    (r'^password_change/$', password_change),
    (r'^password_change_done/$', password_change_done),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': site_media }),
    (r'^register/$', register_page),
    (r'^register/success/$', 'django.views.generic.simple.direct_to_template', { 'template': 'registration/register_success.html' }),

    (r'^save/$', bookmark_save_page),
    (r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),
    (r'^vote/$', bookmark_vote_page),
    (r'^comments/', include('django.contrib.comments.urls')),
)
