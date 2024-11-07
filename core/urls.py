from turtle import update

from django.contrib import admin
from django.urls import path

from main.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path("home/", home_2_view),
    path('talabalar/', talabalar_view),
    path('mualliflar/', mualliflar),
    path('delete/talaba/<int:id>', deleteStudent)
]

