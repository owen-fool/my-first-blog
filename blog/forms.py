from django import forms

from .models import Post, CV

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('personal_info', 'education', 'work_experience',)
