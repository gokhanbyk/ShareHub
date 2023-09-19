# Generated by Django 4.2.4 on 2023-09-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_post_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tag',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
