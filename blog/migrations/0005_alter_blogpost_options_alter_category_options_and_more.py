# Generated by Django 4.2.4 on 2023-09-15 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpost_is_active_alter_category_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('title',)},
        ),
    ]
