# Generated by Django 2.2.14 on 2020-08-09 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_project_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created_at']},
        ),
    ]
