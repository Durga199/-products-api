from django.shortcuts import render
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from django.http import HttpResponse,JsonResponse
from .models import *
from .serializer import *
from django.core import serializers
import json

# API to get all categorys
# url - http://127.0.0.1:8000/category

@api_view(['GET'])
def maincategory(request):

    try:
        category_obj = Category.objects.all()
        serializer = Categoryserializer(category_obj,many=True)
        return Response({'status':200, 'payload':serializer.data})
    except:
        return JsonResponse({"message": "Something Went Wrong"})

# API to get all Sub_category under a category
#You have to give the Category id in the URLS
# url - http://127.0.0.1:8000/subcategory/1

@api_view(['GET'])
def subcategory(request,id):
    try:
        subcategory_obj = Sub_category.objects.filter(category = id)
        serializer = Subcategoryserializer(subcategory_obj, many=True)
        return Response({'status': 200, 'payload': serializer.data})
    except:
        return JsonResponse({"message": "Something Went Wrong"})


# API to get all Poducts under a Sub_category
#You have to give the Sub_Category id in the URLS
# url - http://127.0.0.1:8000/subcat_product/1

@api_view(['GET'])
def subproduct(request,id):
    try:
        prd_obj = Product.objects.filter(subcategory = id)
        serializer = Productserializer(prd_obj, many=True)
        return Response({'status': 200, 'payload': serializer.data})
    except:
        return JsonResponse({"message": "Something Went Wrong"})

# API to get all Poducts under a Category
#This is a POST API . You have to post the category ID to get all the products under that category.
# url - http://127.0.0.1:8000/cat_product/

class Catproduct(APIView):
    def post(self,request):
        cat_id=request.POST.get("cat_id")

        try:
            category_obj = Category.objects.get(id=cat_id)
            subcat_obj=Sub_category.objects.filter(category=category_obj)
            subcat_serializer = serializers.serialize('json', subcat_obj)
            subcat_json = json.loads(subcat_serializer)

            all_subcat_id=[]
            all_products=[]
            for x in subcat_json:
                all_subcat_id.append(x['pk'])
            for x in all_subcat_id:
                product_obj = Product.objects.filter(subcategory=x)
                product_serializer = serializers.serialize('json', product_obj)
                product_json = json.loads(product_serializer)
                if len(product_json)!=0:
                    for x in product_json:
                        all_products.append(x['fields']['prdname'])
            return JsonResponse(all_products,safe=False)

        except:
            return JsonResponse({"message":"Sorry enter a correct category_id"})


# API to POST  Poduct under a Existing sub_Category
#This is a POST API . You have to post the Sub_category ID and Product Name for Inserting new product
# url - http://127.0.0.1:8000/addproduct/

class Addproduct(APIView):
    def post(self,request):
        subcat_id = request.POST.get("subcat_id")
        try:
            if Sub_category.objects.get(id = subcat_id):
               product_name =  request.POST.get('prdname')
               product_instance=Sub_category.objects.get(id = subcat_id)
               product_insert = Product(subcategory = product_instance,prdname = product_name)
               product_insert.save()
               return JsonResponse({"message": " PRODUCT INSERTED SUCCESSFULLY "})
            else:
                return JsonResponse({"message": "Subcategory does not exist"})

        except Exception as e:
            return JsonResponse({"message": "Error in Inserting"})



