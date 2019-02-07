from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from index.models import Test


def index(request):
    name = Test.objects.all()


    context={'a':name}
    return render(request, 'index.html', context=context)

