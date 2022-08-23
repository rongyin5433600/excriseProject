from django.shortcuts import render, HttpResponse, redirect
from UserManagement import models


# Create your views here.


def index(request):
    return render(request, 'index.html')


def depart_list(request):
    depart_queryset = models.DepartInfo.objects.all()
    return render(request, 'depart_list.html', {'depart_queryset': depart_queryset})


def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    depart_name = request.POST.get("inputDepartName")
    depart_title = request.POST.get("inputDepartTitle")
    models.DepartInfo.objects.create(depart_name=depart_name, depart_title=depart_title)
    return redirect("/depart/list")


def depart_delete(request):
    nid = request.GET.get("nid")
    models.DepartInfo.objects.filter(id=nid).delete()
    return redirect("/depart/list")


def depart_edit(request, nid):
    if request.method == "GET":
        queryset = models.DepartInfo.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {'queryset': queryset})
    depart_name = request.POST.get("inputDepartName")
    depart_title = request.POST.get("inputDepartTitle")
    models.DepartInfo.objects.filter(id=nid).update(depart_name=depart_name,depart_title=depart_title)
    return redirect("/depart/list")

