from UserManagement.forms.BootstrapForm import BootstrapForm
from UserManagement.models import PrettyNum
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class PrettyNumForm(BootstrapForm):
    # 字段校验：方法1
    mobile = forms.CharField(
        label='手机号码',
        validators=[RegexValidator(r'^1\d{10}$', '手机号码必须为1开头的11位数字')],
    )
    class Meta:
        model = PrettyNum
        fields = ['mobile', 'price', 'level', 'status']
        # fields = '__all__' 这种写法表示所有字段
    # 为mobile字段添加重复校验
    def clean_mobile(self):
        txt_mobile = self.cleaned_data['mobile']
        is_exists = PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if is_exists:
            raise ValidationError("手机号已存在")
        return txt_mobile
