# Generated by Django 4.2.4 on 2023-08-22 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_benefits_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='benefits',
            old_name='image',
            new_name='cover',
        ),
    ]