from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return f'{instance.slug}/{filename}'


class ProductManager(models.Manager):

    def all(self, *args, **kwargs):
        return super(ProductManager, self).get_queryset().filter(available=True)


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, related_name='category')
    brand = models.ForeignKey('Brand', null=True, on_delete=models.SET_NULL, related_name='brand')
    title = models.CharField(max_length=120)  # nazvanie
    slug = models.SlugField()  # ssylka
    description = models.TextField()  # opisanie
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)  # dostupnost` tovara
    objects = ProductManager()  # esli tovar ne dostupen - ubiraet ego

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})
