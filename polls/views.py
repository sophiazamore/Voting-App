from django.shortcuts import render
from django.http import  HttpResponse
from django.http import JsonResponse
from django.db import models
from django.core.serializers import serialize
import polls.models

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def results(request):
    voting_results = serialize("json", polls.models.Candidate.objects.order_by('total_individual_counts'))
    return HttpResponse(voting_results, content_type='application/json')
# Create your views here.
