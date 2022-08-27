from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import Category,product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
# def index(request):
#     return HttpResponse('Hi I am here')
def allprocat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        products_list=product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        products=paginator.page(page)
    except   (EmptyPage,InvalidPage):
        products=paginator.page(paginator.num_pages)

    return render(request,"Category.html",{'category':c_page,'products':products})
def prodet(request,c_slug,product_slug):
    try:
        prod=product.objects.all().get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'prod':prod})