from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer
from user.serializers import UserdetailSerializer
from rest_framework.response import Response
from .models import myuser
from django.db import transaction
# Create your views here.

class myuserviewset(viewsets.ModelViewSet):
    queryset=myuser.objects.all()
    serializer_class=UserSerializer

class myuserdetailviewset(viewsets.ModelViewSet):
    queryset=myuser.objects.all()
    serializer_class=UserdetailSerializer
    
User = get_user_model()

@api_view(['GET', 'POST'])
@transaction.atomic
def register(request):
    if request.method=='POST':
        form=request.data
        print(form)
        username=form['username']
        password=form['password']
        roles=form['roles']
        response={
            'code':2000
        }
        return Response(response)

@api_view(['GET', 'POST'])
def logout(request):
    if request.method=='POST':
        response={
            'code':2000
        }
        return Response(response)
