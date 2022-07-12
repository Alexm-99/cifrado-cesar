from django import forms

from .models import cifrado

class PostForm(forms.ModelForm):

    class Meta:
        model = cifrado
        fields = ('id', 'nickname', 'message','key')
        #id = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))