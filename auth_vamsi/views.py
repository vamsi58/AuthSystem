from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def health_check(request):
    return JsonResponse("I am up and doing fine")

