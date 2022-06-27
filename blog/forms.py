from django import forms
from .models import Post, Pinterest
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostPosts(forms.ModelForm):
    class Meta:
        model = Post

        fields = [ 'title', 'author', 'photo', 'profile_pic', 'working', 'deadline', 'deadline_date', 'project_date', 'client', 'category', 'body']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'author': forms.Select(
                attrs={'class': 'custom-select' , 'style': 'width: 100%'},
            ),
            'project_date': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'client': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }

class PostPins(forms.ModelForm):
    class Meta:
        model = Pinterest

        fields = [ 'pin_img', 'pin_url', ]