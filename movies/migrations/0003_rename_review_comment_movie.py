# Generated by Django 3.2.13 on 2022-11-23 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='review',
            new_name='movie',
        ),
    ]
