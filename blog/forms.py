from django import forms
from .models import Articles

class ArticlesForms(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'description', 'image', 'category', 'slug')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border-red-500 rounded-2xl outline-none pl-[10px]',
                'placeholder': 'Enter title...'
            }),
            'description': forms.Textarea(attrs={
                'class': '.....'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': '....'
            }),
            'category': forms.Select(attrs={
                'class': '...'
            })
            
        }