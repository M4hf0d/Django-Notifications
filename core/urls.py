from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('v2', views.NotificationListView.as_view(), name='NotificationListView'),
]