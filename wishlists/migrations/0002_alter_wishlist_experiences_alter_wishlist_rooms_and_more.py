# Generated by Django 4.2.5 on 2023-10-14 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiences', '0002_experience_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0005_alter_room_amenities_alter_room_category'),
        ('wishlists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='experiences',
            field=models.ManyToManyField(related_name='wishlists', to='experiences.experience'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='rooms',
            field=models.ManyToManyField(related_name='wishlists', to='rooms.room'),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlists', to=settings.AUTH_USER_MODEL),
        ),
    ]
