from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse

from wms.forms import WarehouseForm
from wms.models import Warehouse, Users
from django.shortcuts import render, redirect, get_object_or_404


def warehouse_list(request):
    warehouse_list1 = Warehouse.objects.all().order_by('id')
    paginator = Paginator(warehouse_list1, 4)  # 每页显示10条记录
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'wms/warehouse/warehouse_list.html', {'page_obj': page_obj})


def warehouse_create(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouse_list')
    else:
        form = WarehouseForm()
    return render(request, 'wms/warehouse/warehouse_form.html', {'form': form})


def warehouse_edit(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            return redirect('warehouse_list')
    else:
        form = WarehouseForm(instance=warehouse)
    return render(request, 'wms/warehouse/warehouse_form.html', {'form': form})


def warehouse_delete(request, pk):
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        try:
            warehouse.delete()
            messages.success(request, '仓库已成功删除')
            return redirect('warehouse_list')
        except Exception as e:
            messages.error(request, f'删除仓库时出错：{e}')
            return render(request, 'wms/warehouse/warehouse_confirm_delete.html', {'warehouse': warehouse})
    return render(request, 'wms/warehouse/warehouse_confirm_delete.html', {'warehouse': warehouse})
