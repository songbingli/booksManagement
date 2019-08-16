from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 网站后台路由
    path('admin/', admin.site.urls),

    # 网站前台路由
    path('', include('bookMS.urls')),
]
