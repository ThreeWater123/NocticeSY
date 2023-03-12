from django import forms
from .models import group



class GroupForm(forms.ModelForm):

    class Meta:
        model=group
        fields=['notice',]
      
        labels={
            'notice':'新通知',
            }
    
        
        