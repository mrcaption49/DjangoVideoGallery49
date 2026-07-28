from django import forms

from .models import Video


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Give your video a title'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'What is this video about?'}),
        }
