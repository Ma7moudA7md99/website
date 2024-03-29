# Generated by Django 5.0.1 on 2024-02-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_skincancer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='VirusC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.FloatField(default=0)),
                ('Sex', models.IntegerField(choices=[(0, 'Male'), (1, 'Female')])),
                ('alb', models.FloatField(default=0)),
                ('alp', models.FloatField(default=0)),
                ('alt', models.FloatField(default=0)),
                ('ast', models.FloatField(default=0)),
                ('bil', models.FloatField(default=0)),
                ('che', models.FloatField(default=0)),
                ('chol', models.FloatField(default=0)),
                ('crea', models.FloatField(default=0)),
                ('ggt', models.FloatField(default=0)),
                ('prot', models.FloatField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='skincancer',
            name='image',
            field=models.ImageField(upload_to='skin cancer/images/2024/2/22'),
        ),
    ]
