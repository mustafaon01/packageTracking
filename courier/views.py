from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .filters import *


# Create your views here.


def index(request):
    return render(request, 'home.html')


def branch(request):
    form = PackageForm()
    form_courier = CourierForm()
    couriers = Courier.objects.all()
    packages = Package.objects.all()
    context = {
        'form': form,
        'form_courier': form_courier,
        'packages': packages,
        'couriers': couriers
    }

    if request.method == 'POST':
        if 'add_courier' in request.POST:
            form_courier = CourierForm(request.POST)
            if form_courier.is_valid():
                form_courier.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                print(form_courier.errors)
        if 'add_package' in request.POST:
            form = PackageForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                print(form.errors)
    return render(request, 'branch.html', context)


def costumer(request):
    packages = Package.objects.none()
    if request.method == "GET":
        filter = Package_filter(request.GET, queryset=packages, request=request)
        if "package_id" in request.GET:
            id = request.GET.get("package_id")
            filter = Package_filter(request.GET,
                                    queryset=Package.objects.filter(package_id=id),
                                    request=request)

    if request.method == "POST":
        id = request.GET.get("package_id")
        filter = Package_filter(request.GET, queryset=Package.objects.filter(package_id=id), request=request)

        if 'time' in request.POST:
            obj = Package.objects.filter(package_id=id).first()
            obj.estimated_arrival_time = request.POST.get('date_update')
            obj.save()

        if 'address' in request.POST:
            obj2 = Package.objects.filter(package_id=id).first()
            obj2.address = request.POST.get('address_update')
            obj2.save()

    context = {
        'packages': packages,
        'filter': filter,
    }

    return render(request, 'costumer.html', context)


def courier(request):
    packages = Package.objects.select_related('courier').all()
    couriers = Courier.objects.all()
    if request.method == "GET":
        courier_filter = Courier_filter(request.GET, queryset=packages, request=request)
        if "courier_id" in request.GET:
            id = request.GET.get("courier_id")
            courier_filter = Courier_filter(request.GET, queryset=Courier.objects.filter(courier_id=id),
                                            request=request)
            print(Courier.objects.filter(courier_id=id))
    context = {
        'packages': courier_filter.qs,
        "couriers": couriers,
        "courier_filter": courier_filter
    }
    return render(request, 'courier.html', context)
