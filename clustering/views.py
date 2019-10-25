from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Clustering (templates/interfaces/index.html)
def cluster(request):
    return HttpResponse(request.POST['PD_CD'])
