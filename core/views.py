from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

from django.views.generic import (ListView, DetailView)
from core.models import Notification


class NotificationListView(ListView):
    model = Notification
    context_object_name = 'notifications'
    paginate_by = 10
    template_name = 'index.html'


    def get_queryset(self):
        print(self.request.user)    
        notifications = self.model.objects.filter(receiver=self.request.user)
        for notification in notifications:
            notification.is_read = True
            notification.save()
        return notifications

    def __str__(self):
            return str(self.get_queryset())
