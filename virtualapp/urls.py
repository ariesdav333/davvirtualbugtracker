"""virtualapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    THIS GETS YOU FROM PAGE TO PAGE 
    Allows us to route to different views using different URLs
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import views as accounts_views
from accounts import urls as accounts_urls
from threads import views as forum_views
from django.views import static
from settings import MEDIA_ROOT



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', index, name="index"),
    url(r'^$', accounts_views.index, name="index"),
    url(r'^$', accounts_views.about, name="about"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^forum/$', forum_views.forum),
    url(r'^profile/$', accounts_views.profile, name="profile"),
    url(r'^registration/$', accounts_views.registration, name="registration"),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$',  forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$',forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),
    url(r'^thread/vote/(?P<thread_id>\d+)/(?P<subject_id>\d+)/$', forum_views.thread_vote, name='cast_vote'),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),  
]
