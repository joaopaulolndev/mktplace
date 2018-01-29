from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('Category', null=True, blank=True, related_name='cat_child', on_delete=False)
    order = models.IntegerField(null=True, blank=True)
    hidden = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, on_delete=False)
    categories = models.ManyToManyField(Category, blank=True, related_name='categories')
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    short_description = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'

    def __str__(self):
        return self.name


class ProductQuestion(models.Model):
    user = models.OneToOneField(User, on_delete=False)
    product = models.ForeignKey('Product', on_delete=False)
    question = models.TextField()
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')

    class Meta:
        verbose_name_plural = 'Product Questions'
        verbose_name = 'Product Question'

    def __str__(self):
        return self.question


class ProductAnswer(models.Model):
    user = models.OneToOneField(User, on_delete=False)
    product_question = models.ForeignKey(ProductQuestion, on_delete=False)
    answer = models.TextField()
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Inactive')

    class Meta:
        verbose_name_plural = 'Answers'
        verbose_name = 'Answer'

    def __str__(self):
        return self.answer
