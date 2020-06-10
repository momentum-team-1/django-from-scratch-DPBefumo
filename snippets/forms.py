from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):
    
    
    class Meta:
        # tags = 
        
        model = Snippet
        fields = [
            'title',
            'description',
            'language',
            'body',
            'tags',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'pa2 f4 w-80 bg-silver'}),
            'description': forms.TextInput(attrs={'class': 'pa2 f4 w-80 bg-silver'}),
            'language': forms.Select(attrs={'class': 'pa2 f4 w-60 bg-silver'}),
            'body': forms.Textarea(attrs={'class': 'pa2 f4 h4 w-90 h5 bg-silver'}),
            'tags': forms.SelectMultiple(attrs={'class': 'pa2 f4 w-60 bg-silver'}),
        } 