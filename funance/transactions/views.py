from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer
from django.shortcuts import render

# Create your views here.
class TransactionListDetailAPIView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionUpdateAPIView(generics.UpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDeleteAPIView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer