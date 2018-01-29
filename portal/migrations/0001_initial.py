# Generated by Django 2.0.1 on 2018-01-29 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('hidden', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=False, related_name='cat_child', to='portal.Category')),
            ],
        ),
    ]
