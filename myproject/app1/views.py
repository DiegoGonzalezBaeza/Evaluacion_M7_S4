from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm

#CRUD Productos
# CREATE Productos
# READ Productos
# UPDATE Productos
# DELETE Productos

# READ Producto (leer todos los registros)
def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'app1/producto_list.html', {'productos': productos})

# READ Producto (lee un registro)
def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'app1/producto_detail.html', {'producto': producto})

# CREATE Producto
def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm()
    return render(request, 'app1/producto_form.html', {'form': form})

# UPDATE Estudiante
def producto_update(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'app1/producto_form.html', {'form': form})

# DELETE Estudiante
def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect('producto_list')
    return render(request, 'app1/producto_confirm_delete.html', {'producto': producto})
