from django import forms
from apps.models import *
from django.core.validators import FileExtensionValidator
from django.forms import TextInput, FileInput

class VideoForm(forms.ModelForm):
    def init(self, *args, **kwargs):
        super (VideoForm, self).init(*args, **kwargs)
        self.fields['titulo'].required = True
        self.fields['titulo'].max_length = 100
        self.fields['titulo'].error_messages = {'required': "Completar campo"}
    
    class Meta:
        model = Video
        fields = ('titulo', 'archivo')
        widgets = {
          'titulo': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del video', 'novalidate':''}),
          'archivo': FileInput(attrs={'class': 'form-control', 'accep':"video/mp4,video/x-m4v,video/*"}),
        }
