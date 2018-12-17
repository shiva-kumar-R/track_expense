from django.shortcuts import render
from .serializers import ExpenseSerializer 
from rest_framework import generics
from .models import expense

# Create your views here.
class ExpenseList(generics.ListCreateAPIView):
    queryset = expense.objects.all()
    serializer_class = ExpenseSerializer