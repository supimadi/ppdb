from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('siswa/<int:pk>/', views.StudentDetailView.as_view(), name="detail-student"),
]
