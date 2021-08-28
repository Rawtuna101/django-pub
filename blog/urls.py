from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.mainpageview, name='mainpage'),
    path('postposts/', views.postposts, name='postposts'),
    path('test/', views.test, name='test'),
    path('test/test2/', views.mainpageview, name='test2'),
]
