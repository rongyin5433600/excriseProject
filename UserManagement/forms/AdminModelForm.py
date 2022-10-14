from UserManagement.forms.BootstrapForm import BootstrapForm
from UserManagement.models import Admin
from django import forms
from django.core.exceptions import ValidationError
from UserManagement.utils import encrypt


class AdminModelForm(BootstrapForm):
    confirm_password = forms.CharField(
        label='确认密码',
        max_length=64,
        widget=forms.PasswordInput  # 设置confirm_password字段为密码输入框
        # widget = forms.PasswordInput(render_value=True)加了render_value参数后报错之后密码框会自动清空
    )

    class Meta:
        model = Admin
        fields = ['adminname', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput,  # 设置password字段为密码输入框
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return encrypt.md5(pwd)

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        cpwd = encrypt.md5(self.cleaned_data.get('confirm_password'))
        if pwd != cpwd:
            raise ValidationError('密码不一致')
        else:
            return cpwd


class AdminResetModelForm(BootstrapForm):
    confirm_password = forms.CharField(
        label='确认密码',
        max_length=64,
        widget=forms.PasswordInput  # 设置confirm_password字段为密码输入框
        # widget = forms.PasswordInput(render_value=True)加了render_value参数后报错之后密码框会自动清空
    )

    class Meta:
        model = Admin
        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput,  # 设置password字段为密码输入框
        }

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        md5_pwd = encrypt.md5(pwd)
        exists = Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError('密码不能与原密码一致')
        return md5_pwd

    def clean_confirm_password(self):
        pwd = self.cleaned_data.get('password')
        cpwd = encrypt.md5(self.cleaned_data.get('confirm_password'))
        if not pwd:
            return cpwd
        else:
            if pwd != cpwd:
                print(pwd, cpwd)
                raise ValidationError('密码不一致')
            else:
                return cpwd
