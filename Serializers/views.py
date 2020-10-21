from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from Serializers.serializers import HelloSerializer
# Create your views here.
class HelloAPIView(APIView):
    serializer_class=HelloSerializer
    """The get method is responsible for handling the get requests"""
    def get(self,request,format=None):
        #always response should be in the form of dictionary
        return Response({'message':"Welcome to First Api demo",'request_type':'Get'})

    def post(self,request,format=None):
        data=request.data.get('name')
        return Response({'message':"Welcome to First Api demo",'request_type':'POST','data':data})

    def put(self,request,format=None):
        data=request.data.get('name')
        return Response({'message':"Welcome to First Api demo",'request_type':'Put','data':data})

    def patch(self,request,format=None):
        data=request.data.get('name')
        return Response({'message':"Welcome to First Api demo",'request_type':'Patch','data':data})

    def delete(self,request,format=None):
        return Response({'message':"Welcome to First Api demo",'request_type':'Delete'})
