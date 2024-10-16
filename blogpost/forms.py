from django import forms
from api.models import Post
from api.models import songdetails

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("category","title","content","slug",)



class songdetailsForm(forms.ModelForm):
    class Meta:
        model=songdetails
        fields=("Category","Song","Title","Featuredimage","Description",)