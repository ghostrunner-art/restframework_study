from django.http import HttpResponse
from rest_framework.views import APIView
# class User(APIView):
#     def get(self,request,*args,**kwargs):
#         return HttpResponse('hello world!')
#     def post(self,request,*args,**kwargs):
#         pass
from .models import Role

from django.http import HttpResponse

class RolesView(APIView):
    def get(self,request,*args,**kwargs):
        # role_obj = Role.objects.get('title')
        # print(role_obj)
        return HttpResponse('**********  OK  **********')








