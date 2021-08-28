# Generated by Django 3.2.6 on 2021-08-27 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcatname', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prdname', models.CharField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.subcategory')),
            ],
        ),
    ]