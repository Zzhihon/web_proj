# Generated by Django 3.2.8 on 2024-08-12 16:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='/profiles/chikawa.jpg', null=True, upload_to='profiles/'),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('skill', models.TextField(blank=True, max_length=100, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
