# Generated by Django 3.1.2 on 2021-03-17 11:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actualites', '0002_event_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateField()),
                ('types', models.CharField(choices=[('urgent', 'Urgent'), ('non_urgent', 'Non_urgent')], default='non_urgent', max_length=10)),
                ('access', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=10)),
                ('attachment', models.CharField(choices=[('pdf', 'Pdf'), ('image', 'Image')], default='pdf', max_length=10)),
                ('image', models.ImageField(max_length=255, upload_to='Images/')),
                ('video', models.FileField(null=True, upload_to='Vidéos/', verbose_name='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateField()),
                ('image', models.ImageField(max_length=255, upload_to=None)),
                ('category', models.CharField(max_length=255)),
                ('attachment', models.CharField(choices=[('pdf', 'Pdf'), ('image', 'Image')], default='pdf', max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
