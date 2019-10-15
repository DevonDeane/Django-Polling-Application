from django.urls import path # to handle urls

from . import views # . = all

app_name = 'pages'

urlpatterns = [
    path('', views.index, name = 'index'),
]
