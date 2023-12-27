from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from.forms import MedForm,CatForm
from firstaid_app.models import Medicine,Category
# Create your views here.
@login_required
def add(request):
    user=request.user
    if user.is_administrator:
        if request.method=='POST':
            name=request.POST.get('name')
            stock=request.POST.get('stock')
            exp_date=request.POST.get('exp_date')
            desc=request.POST.get('desc')
            category=request.POST.get('category')
            category_instance=Category.objects.get(id=category)
            img=request.FILES.get('img')
            medicine=Medicine(name=name,stock=stock,exp_date=exp_date,desc=desc,category=category_instance,img=img)
            medicine.save()
            return redirect('firstaid_app:home')
        return render(request,'add.html')
    else:
        return redirect('login:admin_page')

def update(request,med_id):
    user=request.user
    if user.is_administrator:
        medicine=Medicine.objects.get(id=med_id)
        form=MedForm(request.POST or None,instance=medicine)
        if request.method=='POST':
            if form.is_valid():
                form.save()
                return redirect('/')
        print(form.initial)
        return render(request,'update.html',dict(form=form))
    else:
        return redirect('login:admin_page')

def delete(request,med_id):
    user=request.user
    if user.is_administrator:
        medicine=Medicine.objects.get(id=med_id)
        medicine.delete()
        return redirect('/')
    else:
        return redirect('login:admin_page')
def add_cat(request):
    user=request.user
    if user.is_administrator:
        if request.method=='POST':
            name=request.POST.get('name')
            desc=request.POST.get('desc')
            category=Category(name=name,desc=desc)
            category.save()
            return redirect('/')

        return render(request,'add_cat.html')
    else:
        return redirect('login:admin_page')

def update_cat(request,cat_id):
    user=request.user
    if user.is_administrator:
        category=Category.objects.get(id=cat_id)
        form=CatForm(request.POST or None,instance=category)
        if request.method=='POST':
            if form.is_valid():
                form.save()
                return redirect('/')
        return render(request,'update.html',dict(form=form))
    else:
        return redirect('login:admin_page')

def delete_cat(request,cat_id):
    user=request.user
    if user.is_administrator:
        category=Category.objects.get(id=cat_id)
        category.delete()
        return redirect('/')
    else:
        return redirect('login:admin_page')

