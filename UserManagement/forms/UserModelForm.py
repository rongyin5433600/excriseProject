from UserManagement.forms.BootstrapForm import BootstrapForm
from UserManagement.models import UserInfo


class UserModelForm(BootstrapForm):
    class Meta:
        model = UserInfo
        fields = ['name', 'password', 'age', 'account', 'creat_time', 'depart', 'gender']