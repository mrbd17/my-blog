from django import forms
from .models import Post ,Comment


class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

class UpdatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets ={
            "content":forms.Textarea(attrs={"rows":3, 'placeholder':"Write a comment"})
        }