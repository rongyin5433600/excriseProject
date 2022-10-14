# Generated by Django 3.2.14 on 2022-10-04 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagement', '0013_alter_prettynum_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prettynum',
            name='level',
            field=models.SmallIntegerField(choices=[(4, '4级'), (2, '2级'), (1, '1级'), (3, '3级')], default=1, verbose_name='级别'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(2, '女'), (1, '男')], verbose_name='性别'),
        ),
    ]