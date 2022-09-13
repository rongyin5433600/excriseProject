from django.shortcuts import render, redirect
from UserManagement import models
from UserManagement.utils.pagination import Pagination


# Create your view here.
def index(request):
    return render(request, 'index.html')


# 部门列表
def depart_list(request):
    depart_queryset = models.DepartInfo.objects.all()
    depart_page_pagination = Pagination(request, depart_queryset)
    context = {
        'queryset': depart_page_pagination.page_queryset,
        'page_string': depart_page_pagination.html(),
    }
    return render(request, 'depart_list.html', context)


# 新增部门
def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    depart_name = request.POST.get("inputDepartName")
    depart_title = request.POST.get("inputDepartTitle")
    models.DepartInfo.objects.create(depart_name=depart_name, depart_title=depart_title)
    return redirect("/depart/list")


# 删除部门
def depart_delete(request):
    nid = request.GET.get("nid")
    models.DepartInfo.objects.filter(id=nid).delete()
    return redirect("/depart/list")


# 编辑部门
def depart_edit(request, nid):
    if request.method == "GET":
        queryset = models.DepartInfo.objects.filter(id=nid).first()
        return render(request, "depart_edit.html", {'queryset': queryset})
    depart_name = request.POST.get("inputDepartName")
    depart_title = request.POST.get("inputDepartTitle")
    models.DepartInfo.objects.filter(id=nid).update(depart_name=depart_name, depart_title=depart_title)
    return redirect("/depart/list")
