# Generated by Django 4.2.5 on 2023-11-19 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0002_alter_photo_experience_alter_photo_room_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.URLField(),
        ),
    ]
