from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductInCart


def cart_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    count= data.get("count")

    new_product = ProductInCart.objects.create(session_key = session_key, product_id = product_id, count=count)
    product_total_count = ProductInCart.objects.filter(session_key=session_key, is_active=True).count()
    return_dict["product_total_count"] = product_total_count
    return JsonResponse(return_dict)