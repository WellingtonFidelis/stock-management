"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from stock_management.views import (
    homeView,
    listItemsView,
    createItemView,
    updateItemView,
    deleteItemView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homeView, name="home"),
    path("list-items", listItemsView, name="list-items"),
    path("create-item", createItemView, name="create-item"),
    path("update-item/<str:pk>/", updateItemView, name="update-item"),
    path("delete-item/<str:pk>/", deleteItemView, name="delete-item"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
