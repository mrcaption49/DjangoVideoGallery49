import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('video_file', models.FileField(
                    help_text='Supported formats: mp4, webm, ogg, mov, mkv',
                    upload_to='videos/%Y/%m/%d/',
                    validators=[django.core.validators.FileExtensionValidator(
                        allowed_extensions=['mp4', 'webm', 'ogg', 'mov', 'mkv']
                    )],
                )),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-uploaded_at'],
            },
        ),
    ]
