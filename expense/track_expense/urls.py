from django.urls import path
from . import views

app_name='expenses'

urlpatterns = [
     #/expenses/
    path('api/expense/', views.ExpenseList.as_view(), name='expense_list'),
     #/expenses/pk
    path('api/expense/<int:pk>/', views.ExpenseChange.as_view(), name='expense_edit'),
]