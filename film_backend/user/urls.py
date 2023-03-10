from django.urls import path
from rest_framework import views
from rest_framework_jwt.views import obtain_jwt_token
from .views import myuserviewset,myuserdetailviewset
from .views import register,logout

urlpatterns=[
    path('login/',obtain_jwt_token),
    path('register/',register),
    path('logout/',logout),
    path(r'^user/$',view=myuserviewset),
    path(r'^userdetail',view=myuserdetailviewset)
]