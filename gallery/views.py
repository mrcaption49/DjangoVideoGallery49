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


def edit_video(request, pk):
    """Edit form for updating an existing video's title, description, or file."""
    video = get_object_or_404(Video, pk=pk)

    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, 'Video updated successfully.')
            return redirect('video_detail', pk=video.pk)
    else:
        form = VideoUploadForm(instance=video)

    return render(request, 'gallery/edit.html', {'form': form, 'video': video})


def delete_video(request, pk):
    """Confirmation page + handler for permanently deleting a video."""
    video = get_object_or_404(Video, pk=pk)

    if request.method == 'POST':
        video.delete()
        messages.success(request, 'Video deleted.')
        return redirect('gallery_list')

    return render(request, 'gallery/video_confirm_delete.html', {'video': video})