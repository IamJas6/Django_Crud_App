# Generated by Django 5.0.7 on 2024-07-29 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_alter_createrecord_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createrecord',
            name='phone',
            field=models.CharField(max_length=25),
        ),
    ]