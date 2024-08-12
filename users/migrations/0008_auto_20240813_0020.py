# Generated by Django 3.2.8 on 2024-08-12 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20240813_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='name',
        ),
        migrations.AddField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
