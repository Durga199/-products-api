from rest_framework import serializers
from .models import *

class Categoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Subcategoryserializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        fields = ['subcatname','id']

class Productserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'