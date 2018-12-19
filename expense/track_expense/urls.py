from django.urls import path
from . import views

app_name='expenses'

urlpatterns = [
     #/expenses/
    path('', views.ExpenseList.as_view(), name='expense_list'),
     #/expenses/pk
    path('<int:pk>/', views.ExpenseChange.as_view(), name='expense_edit'),
]