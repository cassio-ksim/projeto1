"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from main.views import index, show, store, destroy, destroy_item, put

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path("<int:id>/", show, name='show'),
    path('nova/tarefa/', store, name='store'),
    path("<int:todo_id>/novo/item/", store, name='store-item'),
    path('<int:todo_id>/excluir/tarefa/', destroy, name='destroy'),
    path('<int:todo_id>/<int:item_id>/excluir/item/', destroy_item, name='destroy-item'),
    path('item/<int:item_id>/edit/', put, name='put-item'),

]
