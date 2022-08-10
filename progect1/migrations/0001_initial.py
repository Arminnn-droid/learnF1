# Generated by Django 3.2.2 on 2022-08-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('age', models.PositiveIntegerField(default=0)),
                ('address', models.GenericIPAddressField(blank=True, null=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=18)),
            ],
        ),
    ]
