# Generated by Django 3.1.1 on 2020-09-09 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(default='', max_length=300),
        ),
    ]
