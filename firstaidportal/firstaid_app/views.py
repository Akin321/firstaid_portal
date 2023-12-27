
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from.models import Category,Medicine

# Create your views here.
@login_required
def home(request,c_slug=None):
    if request.user.is_authenticated:
        cat_id=None
        medicine=None
        if c_slug != None:
            cat_id=get_object_or_404(Category,slug=c_slug)
            medicine=Medicine.objects.all().filter(category=cat_id,available=True)

        else:
            medicine=Medicine.objects.all().filter(available=True)
        return render(request,'home.html',dict(medicine=medicine,category=cat_id))
    else:
        return redirect('login:login')

def meddetial(request,c_slug,m_slug):

    medicine = None
    if c_slug != None:
        medicine=Medicine.objects.get(slug=m_slug)
    return render(request,'medicine.html',dict(medicine=medicine))




