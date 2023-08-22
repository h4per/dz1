from django.db import models

class Courses(models.Model):
    title = models.CharField(
        max_length= 255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='courses/',
        verbose_name='Фото',
        blank=True
    )
    status = models.BooleanField(
        default=True,
        verbose_name="Статус публикации"
    )

    def __str__(self):
        return f"{self.title} - {self.status}"

class Meta:
    verbose_name = 'Курс'
    verbose_name_plural = 'Курсы'
    

class Benefits(models.Model):
    title = models.CharField(
        max_length= 255,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    image = models.ImageField(
        upload_to='benefits/',
        verbose_name='Фото',
        blank=True
    )
    status = models.BooleanField(
        default=True,
        verbose_name="Статус публикации"
    )

    def __str__(self):
        return f"{self.title} - {self.status}"

class Meta:
    verbose_name = 'Преимущество'
    verbose_name_plural = 'Преимущества'