from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.shortcuts import render
from wishlist.models import BarangWishlist
# Create your views here

def show_wishlist(request):
    data = BarangWishlist.objects.all()
    context = {
                'list_barang': data_barang_wishlist,
                'nama': 'Ridho Mulia'
               }
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

