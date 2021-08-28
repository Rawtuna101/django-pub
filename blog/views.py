from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import TemplateView
from .forms import PostPosts
from .models import Post, TimeTracker, Comment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def mainpageview(request):
    site = {
        'url' : 'https://www.rawtuna101.art',
        'todaystart' : '2020-12-19T10:50:00+09:00',
        'switch' : 'false',
        }
    post = Post()
    timetracker = TimeTracker.objects.get(id=1)
    showposts = Post.objects.all()
    return render(request, 
                'blog/layout.html',
                 {'post': post, 
                  'site': site, 
                  'showposts': showposts,
                  'timetracker': timetracker,                  
                 }
            )

def postposts(request):

    if request.method == 'POST':
        form = PostPosts(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('mainpage')
        else:
            return redirect('postposts')
    else:
        form = PostPosts()
        return render(request, 'blog/postposts.html', {'form': form})

def test(request):
    return render(request, 'blog/test.html', {})

@csrf_exempt
def test2(request):
    if 'number' in request.POST:
        num = request.POST['number']

    if num=='1':
      answer = {str(num):"1입니다."}                # json형식으로 넘겨줄 데이터를 만들어준다.
    else:
        answer = {str(num):"1이 아닙니다."}

    return JsonResponse(answer)