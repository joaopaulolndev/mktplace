from django.contrib.auth.models import User
from django.db import models
from s3direct.fields import S3DirectField


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


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=False)
    cpf = models.CharField(max_length=35, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    number = models.CharField(max_length=20, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=15, null=True, blank=True)
    country = models.CharField(max_length=15, null=True, blank=True)
    zipcode = models.CharField(max_length=15, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    remote_customer_id = models.CharField(max_length=255, null=True, blank=True, default='')
    remote_receiver_id = models.CharField(max_length=255, null=True, blank=True, default='')


class ProductImages(models.Model):
    product = models.ForeignKey(Product, related_name='prod_images', on_delete=False)
    images = S3DirectField(dest='product_images')

    class Meta:
        verbose_name_plural = "Images"