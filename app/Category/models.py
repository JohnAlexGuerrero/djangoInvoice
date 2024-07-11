from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    description = models.CharField(("descripcion"), max_length=50, unique=True)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse("Category_detail", kwargs={"pk": self.pk})

