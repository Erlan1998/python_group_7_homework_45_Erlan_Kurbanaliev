"""list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import (
    tasks_view,
    list_view,
    tasks_create_view,
    list_update_view,
    list_delete_view,
    some_delete_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasks_view, name='index_tasks'),
    path('task/<int:id>/', list_view, name='task'),
    path('task/add/', tasks_create_view, name='tasks_create'),
    path('task/<int:id>/update', list_update_view, name='list_update'),
    path('task/<int:id>/delete', list_delete_view, name='list_delete'),
    path('task/some/delete', some_delete_view, name='some_delete')

]
