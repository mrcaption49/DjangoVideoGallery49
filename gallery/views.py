from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VideoUploadForm
from .models import Video


def gallery_list(request):
    """The gallery page: a grid of every uploaded video."""
    videos = Video.objects.all()
    return render(request, 'gallery/gallery_list.html', {'videos': videos})


def video_detail(request, pk):
    """Opens when a video in the gallery is clicked: plays that one video."""
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'gallery/video_detail.html', {'video': video})


def upload_video(request):
    """Upload form for adding a new video with a title and description."""
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            messages.success(request, 'Video uploaded successfully.')
            return redirect('video_detail', pk=video.pk)
    else:
        form = VideoUploadForm()

    return render(request, 'gallery/upload.html', {'form': form})
