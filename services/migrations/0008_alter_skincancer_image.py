# Generated by Django 5.0.1 on 2024-03-23 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_skincancer_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skincancer',
            name='image',
            field=models.ImageField(upload_to='skin cancer/images/2024/3/23'),
        ),
    ]