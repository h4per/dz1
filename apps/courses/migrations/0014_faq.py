# Generated by Django 4.2.4 on 2023-08-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('status', models.BooleanField(default=True, verbose_name='Статус публикации')),
            ],
        ),
    ]