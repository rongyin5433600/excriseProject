# Generated by Django 3.2.14 on 2022-10-09 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0016_auto_20221009_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prettynum',
            name='level',
            field=models.SmallIntegerField(choices=[(2, '2级'), (4, '4级'), (1, '1级'), (3, '3级')], default=1, verbose_name='级别'),
        ),
        migrations.AlterField(
            model_name='prettynum',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '已占用'), (2, '未占用')], default=2, verbose_name='状态'),
        ),
    ]
