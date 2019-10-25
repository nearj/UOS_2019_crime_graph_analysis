from django.urls import path
from . import views

app_name = 'clustering'

urlpatterns = [
    path('', views.cluster, name='cluster')
]