from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False,
        null=True,
    )

    def __str__(self):
        return self.name


class Stock(models.Model):
    category = models.ForeignKey(
        Category, verbose_name="Categoria", on_delete=models.CASCADE, blank=True
    )
    item_name = models.CharField(
        verbose_name="Nome", max_length=50, blank=False, null=True
    )
    quantity = models.IntegerField(
        verbose_name="Quantidade", default="0", blank=False, null=True
    )
    receive_quantity = models.IntegerField(default="0", blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default="0", blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default="0", blank=True, null=True)
    last_updated = models.DateTimeField(verbose_name="Atualizado", auto_now=True)
    created_date = models.DateField(verbose_name="Criado", auto_now_add=True)

    def __str__(self):
        return self.item_name
