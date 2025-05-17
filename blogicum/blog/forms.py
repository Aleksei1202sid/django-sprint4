from django import forms

from .models import Post, Comment, User


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateTimeInput(format='%Y-%m-%d %H:%M:%S',
                                            attrs={'type': 'datetime-local'}),
        }
# Не могу понять зачем вносить format, у меня и так время работало.
# А когда я добавляю format, время замирает при редактировании поста
# в моменте создания поста.

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
