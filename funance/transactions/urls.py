from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.TransactionListDetailAPIView.as_view()),
    path('', views.TransactionListCreateAPIView.as_view())
]