# Generated by Django 4.2.7 on 2024-02-16 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentHub', '0009_remove_rating_rater_remove_rating_resource_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(default='Student', max_length=100),
        ),
    ]
