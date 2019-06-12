from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return "{0}/{1}".format(instance.slug, filename)


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL, related_name='category')
    brand = models.ForeignKey('Brand', null=True, on_delete=models.SET_NULL, related_name='brand')
    title = models.CharField(max_length=120)  # nazvanie
    slug = models.SlugField()
    description = models.TextField()  # opisanie
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'
