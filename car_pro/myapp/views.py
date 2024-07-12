from django.shortcuts import render, redirect, get_object_or_404
from .models import CarManufacturer, CarBrand, SparePart
from .forms import CarManufacturerForm, CarBrandForm, SparePartForm

def index(request):
    manufacturer_form = CarManufacturerForm()
    brand_form = CarBrandForm()
    spare_part_form = SparePartForm()

    edit_manufacturer = edit_brand = edit_spare_part = None

    # Handle form submissions
    if request.method == 'POST':
        if 'save_manufacturer' in request.POST:
            manufacturer_form = CarManufacturerForm(request.POST)
            if manufacturer_form.is_valid():
                manufacturer_form.save()
                return redirect('index')
        elif 'save_brand' in request.POST:
            brand_form = CarBrandForm(request.POST)
            if brand_form.is_valid():
                brand_form.save()
                return redirect('index')
        elif 'save_spare_part' in request.POST:
            spare_part_form = SparePartForm(request.POST)
            if spare_part_form.is_valid():
                spare_part_form.save()
                return redirect('index')
        elif 'edit_manufacturer' in request.POST:
            manufacturer = get_object_or_404(CarManufacturer, id=request.GET.get('edit_manufacturer'))
            manufacturer_form = CarManufacturerForm(request.POST, instance=manufacturer)
            if manufacturer_form.is_valid():
                manufacturer_form.save()
                return redirect('index')
        elif 'edit_brand' in request.POST:
            brand = get_object_or_404(CarBrand, id=request.GET.get('edit_brand'))
            brand_form = CarBrandForm(request.POST, instance=brand)
            if brand_form.is_valid():
                brand_form.save()
                return redirect('index')
        elif 'edit_spare_part' in request.POST:
            spare_part = get_object_or_404(SparePart, id=request.GET.get('edit_spare_part'))
            spare_part_form = SparePartForm(request.POST, instance=spare_part)
            if spare_part_form.is_valid():
                spare_part_form.save()
                return redirect('index')

    if 'edit_manufacturer' in request.GET:
        edit_manufacturer = get_object_or_404(CarManufacturer, id=request.GET.get('edit_manufacturer'))
        manufacturer_form = CarManufacturerForm(instance=edit_manufacturer)
    elif 'delete_manufacturer' in request.GET:
        manufacturer = get_object_or_404(CarManufacturer, id=request.GET.get('delete_manufacturer'))
        manufacturer.delete()
        return redirect('index')

    if 'edit_brand' in request.GET:
        edit_brand = get_object_or_404(CarBrand, id=request.GET.get('edit_brand'))
        brand_form = CarBrandForm(instance=edit_brand)
    elif 'delete_brand' in request.GET:
        brand = get_object_or_404(CarBrand, id=request.GET.get('delete_brand'))
        brand.delete()
        return redirect('index')

    if 'edit_spare_part' in request.GET:
        edit_spare_part = get_object_or_404(SparePart, id=request.GET.get('edit_spare_part'))
        spare_part_form = SparePartForm(instance=edit_spare_part)
    elif 'delete_spare_part' in request.GET:
        spare_part = get_object_or_404(SparePart, id=request.GET.get('delete_spare_part'))
        spare_part.delete()
        return redirect('index')

    manufacturers = CarManufacturer.objects.all()
    brands = CarBrand.objects.all()
    spare_parts = SparePart.objects.all()

    context = {
        'manufacturer_form': manufacturer_form,
        'brand_form': brand_form,
        'spare_part_form': spare_part_form,
        'manufacturers': manufacturers,
        'brands': brands,
        'spare_parts': spare_parts,
        'edit_manufacturer': edit_manufacturer,
        'edit_brand': edit_brand,
        'edit_spare_part': edit_spare_part,
    }
    return render(request, 'index.html', context)
