from django.db import models


class Product(models.Model):
    """Модель Продукт"""
    title = models.CharField(max_length=250, verbose_name='Название')
    model = models.CharField(max_length=150, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода на рынок.')

    def __str__(self):
        return f'{self.title} {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
