# Generated by Django 3.0.8 on 2020-11-09 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClientsManagement', '0021_projectsrequest_project_classification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientsdetail',
            name='profile_image',
            field=models.ImageField(default='MEDIA/clients-profile-images/default.jpg', upload_to='clients-profile-images/'),
        ),
    ]
