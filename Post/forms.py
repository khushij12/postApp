from django import forms

class postInfo(forms.Form):
    title = forms.CharField()
    image = forms.ImageField()