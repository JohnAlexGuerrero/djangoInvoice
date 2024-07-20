from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from django.db.models import Count

from Category.models import Category

# Create your models here.
class Product(models.Model):
    description = models.CharField(("Descripción"), max_length=150, unique=True)
    codebar = models.CharField(("Codigo"), max_length=20, unique=True)
    brand = models.CharField(("Marca"), max_length=150, blank=True, null=True)
    stock = models.IntegerField(("Stock"), default=0)
    unit = models.CharField(("Unidad de medida"), max_length=50, default='Und')
    cost = models.DecimalField(("Costo"), max_digits=10, decimal_places=2, default=0.0)
    price = models.DecimalField(("Precio"), max_digits=10, decimal_places=2, default=0.0)
    weigth = models.FloatField(("Peso"), default=0.0)
    is_active = models.BooleanField(("Activo"), default=1)
    slug = models.SlugField()
    category = models.ForeignKey(Category, verbose_name=("category"), on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    

    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("Products")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("Product_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.description)
        return super().save(*args, **kwargs)
