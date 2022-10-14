from django.shortcuts import render, redirect
from UserManagement.forms.BootstrapForm import BootForm
from django import forms
from UserManagement.utils.encrypt import md5
from UserManagement import models


class LoginForm(BootForm):
    adminname = forms.CharField(
        label='用户名',
        widget=forms.TextInput,
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput,
    )

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # #models.Admin.objects.filter(username=username,password=password).first()
            admin_obj = models.Admin.objects.filter(**form.cleaned_data).first()
            if not admin_obj:
                form.add_error('password', '用户名或密码错误')
                return render(request, 'login.html', {'form': form})
            else:
                # 验证成功之后网站要生成一个随机字符串发给浏览器写到浏览器的cookie中并且写入到session中
                request.session['info'] = {'id': admin_obj.id, 'adminname': admin_obj.adminname}
                return redirect('/admin/list')
        else:
            return render(request, 'login.html', {'form': form})
