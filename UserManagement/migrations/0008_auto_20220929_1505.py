# Generated by Django 3.2.14 on 2022-09-29 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0007_auto_20220929_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prettynum',
            name='level',
            field=models.SmallIntegerField(choices=[(3, '3级'), (1, '1级'), (4, '4级'), (2, '2级')], default=1, verbose_name='级别'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(1, '男'), (2, '女')], verbose_name='性别'),
        ),
    ]
