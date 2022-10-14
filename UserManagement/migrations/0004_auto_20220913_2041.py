# Generated by Django 3.2.14 on 2022-09-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0003_prettynum'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(max_length=32, verbose_name='管理员姓名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
            ],
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='level',
            field=models.SmallIntegerField(choices=[(4, '4级'), (2, '2级'), (3, '3级'), (1, '1级')], default=1, verbose_name='级别'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='status',
            field=models.SmallIntegerField(choices=[(2, '未占用'), (1, '已占用')], default=2, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(2, '女'), (1, '男')], verbose_name='性别'),
        ),
    ]
