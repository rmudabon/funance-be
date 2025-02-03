from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/', views.TransactionListDetailAPIView.as_view()),
    path('<int:pk>/update/', views.TransactionUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.TransactionDeleteAPIView.as_view()),
    path('', views.TransactionListCreateAPIView.as_view())
]