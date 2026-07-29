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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # When editing an existing video, don't force a re-upload just to
        # change the title or description — keep the current file if none
        # is provided.
        if self.instance and self.instance.pk:
            self.fields['video_file'].required = False

    def save(self, commit=True):
        video = super().save(commit=False)
        # If no new file was submitted while editing, keep the existing one.
        if not self.cleaned_data.get('video_file') and self.instance.pk:
            video.video_file = Video.objects.get(pk=self.instance.pk).video_file
        if commit:
            video.save()
        return video