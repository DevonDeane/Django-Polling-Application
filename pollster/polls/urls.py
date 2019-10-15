from django.urls import path # to handle urls

from . import views # . = all

app_name = 'polls'
urlpatterns = [
    path('', views.index, name = 'index'), # '' = /polls -> index view
    path('<int:question_id>/', views.detail, name ='detail'),
    path('<int:question_id>/results/', views.results, name ='results'),
    path('<int:question_id>/vote/', views.vote, name ='vote'),
]
