# Generated by Django 3.2.2 on 2022-08-12 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_number',
            field=models.IntegerField(),
        ),
    ]
