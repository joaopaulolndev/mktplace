# Generated by Django 2.0.1 on 2018-02-12 20:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_productimages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productanswer',
            options={'verbose_name': 'Answer', 'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='productquestion',
            options={'verbose_name': 'Product Question', 'verbose_name_plural': 'Product Questions'},
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=False, related_name='cat_child', to='portal.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.OneToOneField(on_delete=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productanswer',
            name='product_question',
            field=models.ForeignKey(on_delete=False, to='portal.ProductQuestion'),
        ),
        migrations.AlterField(
            model_name='productanswer',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=20),
        ),
        migrations.AlterField(
            model_name='productanswer',
            name='user',
            field=models.OneToOneField(on_delete=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(on_delete=False, related_name='prod_images', to='portal.Product'),
        ),
        migrations.AlterField(
            model_name='productquestion',
            name='product',
            field=models.ForeignKey(on_delete=False, to='portal.Product'),
        ),
        migrations.AlterField(
            model_name='productquestion',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Inactive', max_length=20),
        ),
        migrations.AlterField(
            model_name='productquestion',
            name='user',
            field=models.OneToOneField(on_delete=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=False, to=settings.AUTH_USER_MODEL),
        ),
    ]