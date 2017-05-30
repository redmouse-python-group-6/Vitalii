from django import forms
from comments.models import Comments

# class CommentsForm(forms.Form):
#     title = forms.CharField(max_length=2)
#     body = forms.CharField(widget=forms.Textarea)


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['title', 'body']