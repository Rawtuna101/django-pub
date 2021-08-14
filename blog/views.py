from django.shortcuts import render
from django.views.generic.base import TemplateView

def Mainpageview(request):
    return render(request, 'blog/index.html', {})

# Create your views here.
