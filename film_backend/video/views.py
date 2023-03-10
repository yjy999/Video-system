from django.shortcuts import render
from . import models
from django.views import View
# Create your views here.
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .serializers import VideoSerializer,mainPageSerializer
from django.http import Http404

@api_view(['GET', 'POST'])
def video_list(request):
    videosobject=models.Video.objects.all()
    #return render(request,'video/video_list.html')
    serializer=VideoSerializer(videosobject,many=True)
    print(serializer.data)
    response={
        'code':2000,
        'data':{'urls':serializer.data}
    }
    return Response(response)

class videoonline(APIView):

    def get(self,request,pk):
        videosobject=models.Video.objects.filter(id=pk)
        serializer=VideoSerializer(videosobject,many=True)
        print(serializer.data)
        response={
            'code':2000,
            'data':{'urls':serializer.data}
        } 
        if videosobject:  
            return Response(response)
        else:
            raise Http404("没有该视频")

class videoSearch(APIView):
    def get(self,request):
        keyword=request.GET.get("keyword",None)
        if not keyword:
            response={
            'code':4000,
            'data':'输入不能非空'} 
            return Response(response)
        videoobject=models.Video.objects.filter(Q(title__icontains=keyword))
        if not videoobject:
            response={
            'code':4000,
            'data':'没有该视频'}
            return Response(response)
        serializer=VideoSerializer(videoobject,many=True)
        print(serializer.data)
        response={
            'code':2000,
            'data':{'urls':serializer.data}
        }  
        return Response(response)

@api_view(['GET', 'POST'])
def mainPage_list(request):
    mainPageobject=models.mainPage.objects.all()
    #return render(request,'video/video_list.html')
    serializer=mainPageSerializer(mainPageobject,many=True)
    print(serializer.data)
    response={
        'code':2000,
        'data':{'urls':serializer.data}
    }
    return Response(response)
