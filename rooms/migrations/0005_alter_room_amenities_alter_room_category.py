# Generated by Django 4.2.5 on 2023-10-14 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('rooms', '0004_alter_room_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='amenities',
            field=models.ManyToManyField(related_name='rooms', to='rooms.amenity'),
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='categories.category'),
        ),
    ]
