from django.urls import path
from . import views

app_name = "timeline"

urlpatterns = [
    path('', views.get_api, name="detail"),
    # path('date/', views.display_timeline, name="date")
]