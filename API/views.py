from django.shortcuts import render
from django.http import HttpResponse

from .models import WatchList
from .serializers import *

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

# Create your views here.
@api_view(['GET','POST'])
def list_movies(requset,format = None):
   if requset.method == 'GET':
     movie_list = WatchList.objects.all()
     serializer = WatchlistSerializer(movie_list, many=True)
     return Response(serializer.data)
   
   elif requset.method == 'POST':
     data = requset.data
     serialized = WatchlistSerializer(data = data)

     if serialized.is_valid():
        serialized.save()
        return Response(serialized.data,status=status.HTTP_201_CREATED)
     return Response(serialized.data,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def movie(request,pk,format = None):
    movie = WatchList.objects.get(pk = pk)
    serializer = WatchlistSerializer(movie)
    return Response(serializer.data)



class StreamPlatformList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StreamPlatformDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

# --------------------------------------------------------------------------------
# class StreamPlatformList(APIView):
#    def get(self,request,format = None):
#       stream = StreamPlatform.objects.all()
#       serialized = StreamPlatformSerializer(stream,many= True)
#       return Response(serialized.data,status=status.HTTP_200_OK)
   
#    def post(self,request,format = None):
#        data = request.data
#        serialized = StreamPlatformSerializer(data = data)
#        if serialized.is_valid():
#           serialized.save()
#           return Response(serialized.data,status=status.HTTP_201_CREATED)
#        else:
#           return Response(serialized.data,status=status.HTTP_406_NOT_ACCEPTABLE)
# --------------------------------------------------------------------------------
# class StreamPlatformDetails(APIView):
   
#    def get_object(self,pk):
#       try:
#          platform = StreamPlatform.objects.get(pk = pk)
#          return platform
#       except:
#          return Response(status=status.HTTP_404_NOT_FOUND)

#    def get(self,request,pk,format = None):
#      platform = self.get_object(pk)
#      serialized = StreamPlatformSerializer(platform)
#      return Response(serialized.data,status=status.HTTP_200_OK)
   
#    def put(self,request,pk,format = None):
#         newdata = request.data  
#         serialized = StreamPlatformSerializer(self.get_object(pk),data = newdata)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data,status=status.HTTP_200_OK)
#         else:
#            return Response(serialized.data,status=status.HTTP_304_NOT_MODIFIED)
   
#    def delete(self,request,pk,format = None):
#       self.get_object(pk).delete()
#       return Response(status=status.HTTP_200_OK)

# --------------------------------------------------------------------------------
# @api_view(['GET','POST'])
# def platform_detail(request,format = None):
#     if request.method == 'GET':
#        stream = StreamPlatform.objects.all()
#        serialized = StreamPlatformSerializer(stream,many= True)
#        return Response(serialized.data,status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#        data = request.data
#        serialized = StreamPlatformSerializer(data = data)
#        if serialized.is_valid():
#           serialized.save()
#           return Response(serialized.data,status=status.HTTP_201_CREATED)
#        else:
#           return Response(serialized.data,status=status.HTTP_406_NOT_ACCEPTABLE)
# --------------------------------------------------------------------------------
# @api_view(['GET','PUT','DELETE'])
# def platform(request,pk,format = None):

#     try:
#        platform = StreamPlatform.objects.get(pk = pk)
#     except Exception:
#        return Response(Exception,status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#        serialized = StreamPlatformSerializer(platform)
#        return Response(serialized.data,status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         newdata = request.data  
#         serialized = StreamPlatformSerializer(platform,data = newdata)
#         if serialized.is_valid():
#             serialized.save()
#             return Response(serialized.data,status=status.HTTP_200_OK)
#         else:
#            return Response(serialized.data,status=status.HTTP_304_NOT_MODIFIED)
        
#     elif request.method == 'DELETE':
#        platform.delete()
#        return Response(status=status.HTTP_200_OK)
# --------------------------------------------------------------------------------
    