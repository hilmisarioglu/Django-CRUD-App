# Generated by Django 3.2.9 on 2021-12-16 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to='media/'),
        ),
    ]