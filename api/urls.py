from django.conf.urls import url,include
from . import views,views_study
urlpatterns = [

    # url(r'^01/user', views.User.as_view()),
    url(r'^01/juese/$', views_study.RolesView.as_view()),

]