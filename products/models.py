from django.db import models

# Create your models here.
class Category(models.Model):
    catname = models.CharField(max_length=100)

    def __str__(self):
        return self.catname

class Sub_category(models.Model):

    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcatname = models.CharField(max_length=100)

    def __str__(self):
        return self.subcatname

class Product(models.Model):
    subcategory = models.ForeignKey(Sub_category,on_delete=models.CASCADE)
    prdname = models.CharField(max_length=150)

    def __str__(self):
        return self.prdname


