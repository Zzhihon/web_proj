# Generated by Django 3.2.8 on 2024-08-10 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_project_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]