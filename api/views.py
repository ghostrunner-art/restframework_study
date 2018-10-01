from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from api.models import UserInfo

class User(APIView):
    def get(self,request,*args,**kwargs):
        return HttpResponse('hello world!')

