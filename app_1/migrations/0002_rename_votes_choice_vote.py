# Generated by Django 3.2.2 on 2022-08-10 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='votes',
            new_name='vote',
        ),
    ]
