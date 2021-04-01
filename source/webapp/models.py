from django.db import models
from django.core.validators import MinValueValidator


# category_choices = [('other', 'Разное'), ('sports', 'Спортивне'),  ('Classic', 'Классические'), ('For home', 'Для дома'), ('for study', 'Для учебы')]
class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=2000, null=False, blank=True)
    category = models.ForeignKey('webapp.Categories', related_name='Products', on_delete=models.PROTECT)
    quantity = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(0)])
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)

    class Meta:
        db_table = 'Lists'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.id}. {self.name}'

class Categories(models.Model):
    category = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.category}'