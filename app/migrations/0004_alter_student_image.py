# Generated by Django 3.2.9 on 2021-12-16 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='avatar.jpg', upload_to='student/'),
        ),
    ]