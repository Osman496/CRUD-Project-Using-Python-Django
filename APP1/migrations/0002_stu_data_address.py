# Generated by Django 5.0.4 on 2024-11-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stu_data',
            name='address',
            field=models.CharField(default='Not provided', max_length=70),
        ),
    ]
