from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from threads.views import new_thread,show_thread,new_group

from ajax_select import urls as ajax_select_urls

from django.contrib import admin
admin.autodiscover()

from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'expow.views.home', name='home'),
    # url(r'^expow/', include('expow.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^$',TemplateView.as_view(template_name='base.html'),name='base'),

    (r'^lookups/', include(ajax_select_urls)),

    url(r'^admin/', include(admin.site.urls)),
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),

    (r'^tinymce/', include('tinymce.urls')),

    ##########################################
    ## Threads
    ##########################################
    url(r'^thread/(?P<thread_id>\d+)/$',show_thread, name='show_thread'),
    url(r'^newthread/$',new_thread, name='new_thread'),

    ##########################################
    ## Groups
    ##########################################
    url(r'^newgroup/$',new_group, name='new_group'),

    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
    #(r'^%s/' % settings.DAJAX_MEDIA_PREFIX, include('dajax.urls')),

)
