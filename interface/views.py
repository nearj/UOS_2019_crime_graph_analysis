from django.shortcuts import render
from .models import Trial

def list(request):
    trials = Trial.objects.all()
    context = { 'trials': trials}
    return render(request, 'interfaces/index.html', context)

def results(request, trial_id):
    trial = Trial.objects.get(pk=trial_id)
    context = { 'trial': trial }  
    return render(request, 'interfaces/result.html', context)
