from django.http import HttpResponse
#import importlib.util
#product = importlib.util.spec_from_file_location("product", "/model/product.py")
from django.core import serializers
from mysite.model.product import Product

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request):
    p = Product('best product')
    p2 = Product('good product')
    p_list = [p, p2]
    #return HttpResponse("Detail Page")
    jsonResult = serializers.serialize('json', p_list)
    return HttpResponse(jsonResult, content_type="text/json-comment-filtered")