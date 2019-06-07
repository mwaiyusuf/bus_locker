from django import forms
from .models import Image,Review,Profile,Project 
from django.forms import ModelForm,Textarea,IntegerField  

# class NewImageForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         exclude = ['user',]

class NewBusForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user',]

class UpdatebioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]

# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = [ 'usability_rating', 'design_rating', 'content_rating' , 'comment']
#         widgets = {
#             'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
#         }
        
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
