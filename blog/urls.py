from django.urls import path
from . import views
from django.conf.urls import include
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.mainpageview, name='mainpage'),
    path('postposts/', views.postposts, name='postposts'),
    path('postpins/', views.postpins, name='postpins'),
    path('test/', views.test, name='test'),
    path('test/test2/', views.mainpageview, name='test2'),
    path('comment/', views.comment, name='comment'),
    path('contact/', views.contact, name='contact'),
    path('rkgk/', views.rkgk, name='rkgk'),
    path('mana/', TemplateView.as_view(template_name='blog/mana.html')),
]
