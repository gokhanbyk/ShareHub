# Generated by Django 4.2.4 on 2023-09-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
