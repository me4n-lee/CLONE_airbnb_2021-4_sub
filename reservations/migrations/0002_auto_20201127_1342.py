# Generated by Django 2.2.5 on 2020-11-27 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='checj_out',
            new_name='check_out',
        ),
    ]