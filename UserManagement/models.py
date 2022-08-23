from django.db import models


# Create your models here.


class DepartInfo(models.Model):
    """  部门表  """
    depart_name = models.CharField(verbose_name="部门名称", max_length=32)
    depart_title = models.CharField(verbose_name="部门标题", max_length=32)


class UserInfo(models.Model):
    """  员工表  """
    name = models.CharField(verbose_name="员工姓名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    creat_time = models.DateTimeField(verbose_name="入职时间")
    # 员工所属部门为外键约束
    # -to表示需要与哪张表关联
    # -to_field表示要与哪一列关联
    # django会自动关联列名最后生产的表中这一列的名称是depart_id
    # 部门表被删除
    # 1、级联删除
    # depart = models.ForeignKey(to="DepartInfo", to_field="id", on_delete=models.CASCADEF)
    # 2、置空
    depart = models.ForeignKey(to="DepartInfo", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)
    # 性别
    # 在django中设置约束ma
    gender_choices = {
        (1, "男"),
        (2, "女"),
    }
    gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
