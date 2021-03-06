# Generated by Django 2.2.14 on 2020-08-10 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_auto_20200809_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='services',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
