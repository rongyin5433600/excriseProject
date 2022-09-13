from django.shortcuts import render, redirect
from UserManagement import models
from UserManagement.utils.pagination import Pagination
from UserManagement.forms.UserModelForm import UserModelForm


# Create your view here.

# 用户列表
def user_list(request):
    user_queryset = models.UserInfo.objects.all()
    user_page_pagination = Pagination(request, user_queryset)
    context = {
        'queryset': user_page_pagination.page_queryset,
        'page_string': user_page_pagination.html(),
    }
    return render(request, 'user_list.html', context)


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
        return redirect('/user/list')


def user_modelform_add(request):
    # 用户使用GET请求访问页面时的页面展示
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_modelform_add.html', {'form': form})
    # 用户使用post提交数据，数据校验以及保存
    else:
        form = UserModelForm(data=request.POST)
        if form.is_valid():
            # {'name': 'rong123', 'password': '234', 'age': 34, 'account': Decimal('0'),
            # 'creat_time': datetime.datetime(2011, 1, 1, 0, 0, tzinfo=<UTC>),
            # 'depart': <DepartInfo: 销售部>, 'gender': 1}
            print(form.cleaned_data)
            form.save()
            return redirect('/user/list')
        else:
            print(form.errors)
            return render(request, 'user_modelform_add.html', {'form': form})


def user_edit(request, nid):
    # 根据id从数据库中获取对应的数据
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})
    else:
        # instance=row_object此处指定form需要更新指定的数据而不是新增数据
        form = UserModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            # 如果需要保存用户输入以外的数据
            # form.instance.字段名 == 值
            form.save()
            return redirect('/user/list')
        else:
            return render(request, 'user_edit.html', {'form': form})


def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')
