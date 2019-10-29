from django.urls import path
from . import views

app_name = 'interfaces'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:trial_id>/', views.results, name='results')
]