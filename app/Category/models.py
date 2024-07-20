from django.db import models
from django.db.models import Count

from django.utils.text import slugify

from django.urls import reverse, reverse_lazy


# Create your models here.
class Category(models.Model):
    description = models.CharField(("descripcion"), max_length=50, unique=True)
    slug = models.SlugField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})
    
    def get_items_url(self):
        return reverse_lazy("by_category", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.description)
        return super().save(*args, **kwargs)
    
    def getCountProducts(self):
        count_items = Category.objects.filter(product__is_active=True).filter(id=self.id).count()
        return count_items