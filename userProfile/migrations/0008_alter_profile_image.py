# Generated by Django 5.0.1 on 2024-02-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0007_alter_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/'),
        ),
    ]
