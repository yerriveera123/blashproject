from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from app.serializers import *
from rest_framework import status
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.


class EngagementPostview(APIView):
    def get(self,request,tenant_id):
        posts=EngagementPost.objects.filter(id=tenant_id)
        serializer=EngagementPostSerializer(posts,many=True)
        return Response(serializer.data)
class CreateProductView(APIView):
    def post(self,request):
        serializer=EngagementPostProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class CreateCollectionView(APIView):
    def post(self,request):
        serializer=CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
class TopPostsView(APIView):
    def get(Self,request,tenant_id):
        posts=EngagementPost.objects.filter(tenant_id=tenant_id).order_by('-views')[:5]
        serializer=EngagementPostSerializer(posts,many=True)
        return Response(serializer.data)
    
class TopProductView(APIView):
    def get(self,request,tenant_id):
        products=EngagementPostProduct.objects.filter(tenant_id=tenant_id).order_by('-views')[:5]
        serializer=EngagementPostProductSerializer(products,many=True)
        return Response(serializer.data)
    
        

        

