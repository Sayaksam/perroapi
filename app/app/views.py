from django.shortcuts import render
from django.http import HttpResponse


def justatest(request):
    return HttpResponse("Welcome to Perroworld!!!! Test Successful :) ")
