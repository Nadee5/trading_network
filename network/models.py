from django.db import models
from products.models import Product


NULLABLE = {'blank': True, 'null': True}


class NetworkNode(models.Model):
    """Модель торговой сети"""

    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=255, verbose_name='Название')

    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=150, verbose_name='Город')
    street = models.CharField(max_length=150, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')

    products = models.ManyToManyField(Product, related_name='network_nodes', verbose_name='Продукты')

    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Поставщик')
    level = models.IntegerField(choices=LEVEL_CHOICES, **NULLABLE, verbose_name='Уровень звена')
    debt = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Задолженность')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.name}, {self.email}, {self.country}'

    def save(self, *args, **kwargs):
        """Переопределение метода для автоматической установки уровня иерархии звена."""
        if self.supplier:
            # Если у поставщика объекта уровень 2, то уровень сохраняется и для текущего звена (max level)
            if self.supplier.level == 2:
                self.level = 2
            self.level = self.supplier.level + 1
        else:
            # Если у объекта нет поставщика, он считается заводом (уровень 0)
            self.level = 0
        super(NetworkNode, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'
        ordering = ('id',)
