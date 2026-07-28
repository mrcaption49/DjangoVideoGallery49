# Video Gallery (Django)

A simple Django app for uploading videos and browsing them in a gallery.
Click any video in the gallery to open it on its own playback page.

## Features
- Upload a video with a title and description
- Gallery page showing all uploaded videos as a grid
- Click a video -> opens a dedicated page that plays it
- Django admin support for managing videos too

## Setup

```bash
# 1. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up the database
python manage.py migrate

# 4. (Optional) Create an admin user
python manage.py createsuperuser

# 5. Run the server
python manage.py runserver
```

Then open:
- http://127.0.0.1:8000/ — the gallery
- http://127.0.0.1:8000/upload/ — upload a new video
- http://127.0.0.1:8000/admin/ — Django admin (manage/delete videos)

## Project structure

```
videogallery/
├── manage.py
├── requirements.txt
├── videogallery/        # project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── gallery/              # the app
    ├── models.py         # Video model (title, description, video_file, uploaded_at)
    ├── forms.py          # upload form
    ├── views.py          # gallery_list, video_detail, upload_video
    ├── urls.py
    ├── admin.py
    ├── migrations/
    └── templates/gallery/
        ├── base.html
        ├── gallery_list.html
        ├── video_detail.html
        └── upload.html
```

## Notes for going to production
- Change `SECRET_KEY` in `videogallery/settings.py` and set `DEBUG = False`.
- Set `ALLOWED_HOSTS` to your real domain(s).
- Serve `/media/` (uploaded videos) via Nginx/Apache or object storage (S3, etc.)
  instead of Django — Django only serves media itself in `DEBUG` mode.
- Allowed video file extensions are restricted to mp4, webm, ogg, mov, mkv
  (edit `ALLOWED_VIDEO_EXTENSIONS` in `gallery/models.py` to change this).
- Consider adding a max file-size check in `forms.py` if you want to cap
  upload sizes, and configure your web server/proxy's max body size to match.
