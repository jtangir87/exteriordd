# Generated by Django 2.2.14 on 2020-08-10 14:21

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200810_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='page_css',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='page_js',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]