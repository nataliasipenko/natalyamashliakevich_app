# Generated by Django 3.2.4 on 2021-06-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientpost',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='clientpost',
            name='status',
        ),
        migrations.AlterField(
            model_name='clientpost',
            name='author',
            field=models.CharField(max_length=80),
        ),
    ]
