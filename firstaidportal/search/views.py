from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from firstaid_app.models import Medicine
# Create your views here.
@login_required
def search(request):
    medicine=None
    elem=None
    if 'Search' in request.GET:
        elem=request.GET.get('Search')
        medicine=Medicine.objects.all().filter(Q(name__contains=elem))
    return render(request,'search.html',{'medicine':medicine,'elem':elem})