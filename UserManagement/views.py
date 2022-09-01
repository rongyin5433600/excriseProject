from django.shortcuts import render, HttpResponse, redirect
from UserManagement import models


# Create your views here.


def index(request):
    return render(request, 'index.html')


# 部门列表
def depart_list(request):
    depart_queryset = models.DepartInfo.objects.all()
    return render(request, 'depart_list.html', {'depart_queryset': depart_queryset})


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


# 用户列表
def user_list(request):
    user_queryset = models.UserInfo.objects.all()
    '''
        #用python代码获取数据库数据
        for obj in user_queryset:
            print(obj.id, obj.name, obj.password, obj.age, obj.account, obj.creat_time.strftime("%Y-%m-%d"),
                  obj.depart.depart_name, obj.gender, obj.get_gender_display())   
    '''

    return render(request, 'user_list.html', {'user_queryset': user_queryset})


def user_add(request):
    if request.method == 'GET':
        content = {
            'gender_choices': models.UserInfo.gender_choices,
            'depart_list': models.DepartInfo.objects.all(),
        }
        return render(request, 'user_add.html', content)
    else:
        name = request.POST.get('name')
        password = request.POST.get('password')
        age = request.POST.get('age')
        account = request.POST.get('account')
        ctime = request.POST.get('ctime')
        depart_id = request.POST.get('depart_id')
        gender = request.POST.get('gender')
        models.UserInfo.objects.create(name=name, password=password, age=age, account=account, creat_time=ctime,
                                       depart_id=depart_id, gender=gender)
        return redirect("/user/list")
