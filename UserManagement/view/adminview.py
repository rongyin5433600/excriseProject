from django.shortcuts import render, redirect
from UserManagement import models
from UserManagement.utils.pagination import Pagination
from UserManagement.forms.AdminModelForm import AdminModelForm,AdminResetModelForm


def admin_list(request):
    data_dict = {}
    ''' 页面查询条件 '''
    search_data = request.GET.get('adminname')
    if search_data:
        data_dict['adminname__contains'] = search_data
    else:
        search_data = ''
        data_dict['adminname__contains'] = search_data

    queryset = models.Admin.objects.filter(**data_dict)

    pagination = Pagination(request, queryset)

    prettynum_queryset = pagination.page_queryset

    page_string = pagination.html()

    context = {'prettynum_queryset': prettynum_queryset, 'search_data': search_data, 'page_string': page_string,
               'page': pagination.page}

    return render(request, 'admin_list.html', context)


def admin_add(request):
    if request.method == 'GET':
        form = AdminModelForm()
        return render(request, 'change.html', {'form': form, 'title': '新增管理员'})
    else:
        form = AdminModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/list?page=1')
        else:
            return render(request, 'change.html', {'form': form, 'title': '新增管理员'})


def admin_edit(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html', {'msg': '数据不存在'})
    if request.method == 'GET':
        form = AdminModelForm(instance=row_object)
        return render(request, 'change.html', {'form': form, 'title': '编辑管理员'})
    else:
        form = AdminModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect('/admin/list?page=1')
        else:
            return render(request, 'change.html', {'form': form, 'title': '编辑管理员'})
    return render(request, 'change.html')


def admin_delete(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html', {'msg': '数据不存在'})
    row_object.delete()
    return redirect('/admin/list')


def admin_reset(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'error.html', {'msg': '数据不存在'})
    if request.method == 'GET':
        form = AdminResetModelForm()
        return render(request, 'admin_reset.html', {'form': form, 'title': '密码重置'})
    else:
        form = AdminResetModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect('/admin/list?page=1')
        else:
            return render(request, 'admin_reset.html', {'form': form, 'title': '密码重置'})
    return render(request, 'admin_reset.html')
