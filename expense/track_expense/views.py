from django.shortcuts import render
from .serializers import ExpenseSerializer 
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from .models import Expense

# Create your views here.
class ExpenseList(APIView):
    def get(self,request):
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ExpenseChange(APIView):
    def get(self,request,pk):
        try:
            expense = Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return HttpResponse(status=404)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def put(self,request,pk):
        try:
            expense = Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return HttpResponse(status=404)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def delete(self,request,pk):
        try:
            expense = Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return HttpResponse(status=404)
        expense.delete()
        return HttpResponse(status=204)
