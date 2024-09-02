from django.db import models

# Create your models here.
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse
# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='distribution_products', blank=True)

    def get_url(self):
        return reverse('e_app:product_by_category', args=[self.slug])

    class meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return '{}'.format(self.name)


class Product(models.Model):
    name = models.CharField(max_length=220, unique=True)
    slug = models.SlugField(max_length=220, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='distribution_products',blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('e_app:product_details', args=[self.category.slug,self.slug])

    class meta:
        ordering = ('name',)
        verbose_name = 'category_item'
        verbose_name_plural = 'categories_item'

    def __str__(self):
        return '{}'.format(self.name)