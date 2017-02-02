from django.conf.urls import url,include
from bookmark.views import BookmarkLV,BookmarkDV

urlpatterns = [
    #Class-based views
    url(r'^$',BookmarkLV.as_view(),name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(),name='detail'),

]
