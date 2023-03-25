from django.urls import path

from .views import *
from .views import ClientView

urlpatterns = [
    path("", DashboardView.as_view()),
    path("client/", ClientView.as_view(), name="clients"),
    path("client/add/", NewClientView.as_view()),
    path("client/<pk>/edit/", DetailClientView.as_view()),


    # path('<pk>/update',ClientUpdateView.as_view())

]
