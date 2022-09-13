from django.shortcuts import render, redirect
from UserManagement import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from UserManagement.utils.pagination import Pagination
from UserManagement.forms.PrettyNumForm import PrettyNumForm


# Create your view here.

def prettynum_list(request):
    # for i in range(1, 300):
    #     models.PrettyNum.objects.create(mobile='1338979876', price=200, level=2, status=2)
    data_dict = {}
    ''' 页面查询条件 '''
    search_data = request.GET.get('mobile')
    if search_data:
        data_dict['mobile__contains'] = search_data
    else:
        search_data = ''
        data_dict['mobile__contains'] = search_data
    queryset = models.PrettyNum.objects.filter(**data_dict)

    pagination = Pagination(request, queryset)

    prettynum_queryset = pagination.page_queryset

    page_string = pagination.html()

    context = {'prettynum_queryset': prettynum_queryset, 'search_data': search_data, 'page_string': page_string,
               'page': pagination.page}

    return render(request, 'prettynum_list.html', context)


def prettynum_add(request):
    if request.method == 'GET':
        form = PrettyNumForm()
        return render(request, 'prettynum_add.html', {'form': form})
    else:
        form = PrettyNumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/prettynum/list?page=1')
        else:
            return render(request, 'prettynum_add.html', {'form': form})


class PrettyNumEditForm(forms.ModelForm):
    # 字段校验：方法1
    mobile = forms.CharField(
        # disabled=True,  # 增加disable选项后前台页面只显示不能修改
        label='手机号码',
        validators=[RegexValidator(r'^1\d{10}$', '手机号码必须为1开头的11位数字')],
    )

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
        # fields = '__all__' 这种写法表示所有字段

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {'class': 'form-control', 'placeholder': field.label}

    # 编辑时的重复校验需要排除自身数据
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        is_exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if is_exists:
            raise ValidationError("手机号已存在")
        return txt_mobile


def prettynum_edit(request, nid):
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = PrettyNumEditForm(instance=row_object)
        return render(request, 'prettynum_edit.html', {'form': form})
    else:
        form = PrettyNumEditForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect('/prettynum/list')
        else:
            return render(request, 'prettynum_edit.html', {'form': form})


def prettynum_delete(request, nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/prettynum/list?page=1')
