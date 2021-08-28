from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('category',maincategory),
    path('subcategory/<int:id>',subcategory),
    path('subcat_product/<int:id>',subproduct),
    path('cat_product/',Catproduct.as_view()),
    path('addproduct/',Addproduct.as_view()),

]