from django.shortcuts import get_object_or_404, render
from .models import Categoria, Product
# Create your views here.

def index(request):
    product_list = Product.objects.order_by('nombre')[:6]
    context = {
        'product_list' : product_list,
        }
    return render(request, 'index.html', context)
def producto(request, producto_id):
    producto = get_object_or_404(Product, pk=producto_id)
    category_list = Categoria.objects.order_by('nombre')
    return render(request, 'producto.html', {'producto' : producto, 'category_list' : category_list})