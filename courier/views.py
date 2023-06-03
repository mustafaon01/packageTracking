from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .filters import *


# Create your views here.


def index(request):
    return render(request, 'home.html')


def courier(request):
    return render(request, 'courier.html')


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

    time_update = UpdateTime()
    address_update = UpdateAddress()
    if request.method == "POST":
        id = request.GET.get("package_id")
        filter = Package_filter(request.GET, queryset=Package.objects.filter(package_id=id), request=request)
        if 'time' in request.POST:
            time_update = UpdateTime(request.POST)
            if time_update.is_valid():
                obj = Package.objects.filter(package_id=id).first()
                obj.estimated_arrival_time = time_update.cleaned_data["estimated_arrival_time"]
                obj.save()
            else:
                print(time_update.errors)
        if 'address' in request.POST:
            address_update = UpdateAddress(request.POST)
            if address_update.is_valid():
                print("valid")
                obj2 = Package.objects.filter(package_id=id).first()
                obj2.address = address_update.cleaned_data["address"]
                obj2.save()
            else:
                print(address_update.errors)

    context = {
        'packages': packages,
        'filter': filter,
        'time_update': time_update,
        'address_update': address_update
    }


    return render(request, 'costumer.html', context)