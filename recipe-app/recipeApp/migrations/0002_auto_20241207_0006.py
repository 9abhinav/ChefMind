# Generated by Django 3.2.5 on 2024-12-06 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipeApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='updated_at',
        ),
    ]