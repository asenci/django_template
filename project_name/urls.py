from django.contrib import admin
from django.urls import path

import project_name.main.views


urlpatterns = [
    path('', project_name.main.views.index, name='index'),
    path('admin/', admin.site.urls),
]
