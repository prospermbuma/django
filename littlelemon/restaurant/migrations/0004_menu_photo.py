# Generated by Django 5.2.1 on 2025-05-25 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_menu_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='photo',
            field=models.ImageField(default='', upload_to='menu_photos/'),
        ),
    ]
