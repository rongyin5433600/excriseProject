"""excriseProject URL Configuration

The `urlpatterns` list routes URLs to view. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function view
    1. Add an import:  from my_app import view
    2. Add a URL to urlpatterns:  path('', view.home, name='home')
Class-based view
    1. Add an import:  from other_app.view import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from UserManagement.view import userviews, departviews, prettynumviews, adminview, accountview

urlpatterns = [
    # path('admin/', admin.site.urls),
    # 部门管理
    path('depart/list', departviews.depart_list),
    path('depart/add', departviews.depart_add),
    path('depart/delete', departviews.depart_delete),
    path('depart/<int:nid>/edit', departviews.depart_edit),
    # 用户管理
    path('user/list', userviews.user_list),
    path('user/add', userviews.user_add),
    path('user/modelform/add', userviews.user_modelform_add),
    path('user/<int:nid>/edit', userviews.user_edit),
    path('user/<int:nid>/delete', userviews.user_delete),
    # 号码管理
    path('prettynum/list', prettynumviews.prettynum_list),
    path('prettynum/add', prettynumviews.prettynum_add),
    path('prettynum/<int:nid>/edit', prettynumviews.prettynum_edit),
    path('prettynum/<int:nid>/delete', prettynumviews.prettynum_delete),
    # 管理员管理
    path('admin/list', adminview.admin_list),
    path('admin/add', adminview.admin_add),
    path('admin/<int:nid>/edit', adminview.admin_edit),
    path('admin/<int:nid>/delete', adminview.admin_delete),
    path('admin/<int:nid>/reset', adminview.admin_reset),
    # 登录
    path('login', accountview.login),
]
