from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^blog/(?P<slug>[\w-]+)/$', views.detail_thoughts, name='detail_thoughts'),
    url(r'^work/(?P<slug>[\w-]+)/$', views.detail_work, name='detail_work'),
    url(r'^photo/(?P<slug>[\w-]+)/$', views.detail_photos, name='detail_photos'),
    url(r'^film/(?P<slug>[\w-]+)/$', views.detail_videos, name='detail_videos'),
]