# Generated by Django 3.1.2 on 2021-03-17 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('speaker', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('update_at', models.DateField()),
                ('date', models.DateField()),
                ('url', models.URLField(max_length=2000)),
                ('begin', models.TimeField()),
                ('end', models.TimeField()),
                ('image', models.ImageField(max_length=255, upload_to=None)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
    ]