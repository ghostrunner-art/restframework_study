from rest_framework.views import APIView
''''''
# ################## rest_framework功能入口 ################## #
# from rest_framework.versioning import BaseVersioning #版本控制
# from rest_framework.authentication import BaseAuthentication #认证流程
# from rest_framework.permissions import BasePermission #权限设置
# from rest_framework.throttling import BaseThrottle #节流：访问/节流 设置
'''
以上功能使用都是通过自己实现一个需求类，继承相应的Base...基类
并必须实现基类中约束的方法。
在将要使用的CBV类中定义全局变量(在类APIView中查找全局变量名)。
原理查看dispatch中的源码，requset被重新封装了。
继承APIView的CBV类里面所有内容之前前先执行self.dispatch
'''

# from api.models import UserInfo,UserGroup,UserToker,Role

# ################## rest_framework功能入口 -- 解析 ################## #
'''
from rest_framework.parsers import JSONParser,FormParser
在CBV功能类中配置 parser_classes = [JSONParser,]就代表允许用户发送json类型的数据。

class User(APIView):
    def post(self,request,*args,**kwargs):
        parser_classes = [JSONParser,FormParser] #这块接收的是前台发来的 json数据 和form表单POST数据
        print(request.data)                      #如果收到的是json数据 他返回的是个字典
        return HttpResponse('hello world!')
        # self.dispatch
'''
# ################## rest_framework功能入口 -- 序列化 ################## #
from api.models import UserInfo,UserGroup,UserToker,Role

from django.http import HttpResponse
from rest_framework import serializers
import json

class RolesSerializers(serializers.Serializer):
    tt = serializers.CharField(source='title',)
    class Meta:
        model = UserInfo
        fields = '__all__'
        depth = 1

class UserSerializers(serializers.Serializer):
    cc = serializers.CharField(source='user_type',)
    bb = serializers.CharField(source='get_user_type_display',)

class RolesView(APIView):
    def get(self,request,*args,**kwargs):
        # role_obj = Role.objects.get('title')
        # print(role_obj)
        rol = Role.objects.all()
        userinfo2 = UserInfo.objects.all()
        ser = RolesSerializers(instance=rol,many=True)
        userinfo2 = UserSerializers(instance=userinfo2,many=True)
        ser11 = json.dumps(ser.data,ensure_ascii=False)
        ser22 = json.dumps(userinfo2.data,ensure_ascii=False)
        print(ser11)
        return HttpResponse(ser22)

from rest_framework.pagination import PageNumberPagination












