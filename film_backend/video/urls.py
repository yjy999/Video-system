from django.urls import path
from django.conf.urls import url
from video import views
from .views import video_list,mainPage_list
urlpatterns=[
    path('list/',video_list),
    url(r'^online/(?P<pk>[0-9]+)$',views.videoonline.as_view()),
    url('search/',views.videoSearch.as_view()),
    path('mainPage/',mainPage_list),
]