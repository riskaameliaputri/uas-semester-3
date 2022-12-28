from django.contrib import admin
from django.urls import path
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blogs),
    path('tambah/', Data_baru, name='data_baru'),
]
