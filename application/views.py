from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Sum
from django.http import JsonResponse
from rest_framework import viewsets
from django.shortcuts import render
# Create your views here.


def htmlPage(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("This is my first application")


class expenseApiView(APIView):
    serializer_class = TrackerSerializer

    def get(self, request):
        allExpense = Tracker.objects.all().values()
        return Response({"Message": "List of expenses", "expenses": allExpense})

    def post(self, request):
        print("Request data is", request.data)
        serializer_obj = TrackerSerializer(data=request.data)
        if serializer_obj.is_valid():

            Tracker.objects.create(id=serializer_obj.data.get("id"),
                                   buy=serializer_obj.data.get("buy"),
                                   reason=serializer_obj.data.get("reason"))
        expense = Tracker.objects.filter(id=request.data["id"]).values()
        return Response({"Message": "expense added", "expense": expense})


class AccountViewSet(viewsets.ModelViewSet):
    queryset = accounts.objects.all()
    serializer_class = BankSerializer


def total_amount(request):
    total = accounts.objects.aggregate(Sum('amount'))['amount__sum']
    amount_spend = Tracker.objects.aggregate(Sum('buy'))['buy__sum']

    amount_left = total - amount_spend
    return JsonResponse({'total_amount': total,
                          'amount_spend': amount_spend, 
                        "amount_left": amount_left
                          })
