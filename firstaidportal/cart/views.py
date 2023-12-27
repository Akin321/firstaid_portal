from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from firstaid_app.models import Medicine
from . models import Cart,Cart_items,Req_items
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from login.models import CustomUser
# Create your views he
@login_required

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def addcart(request,med_id):
    if request.user.is_authenticated:
        medicine=Medicine.objects.get(id=med_id)
        print(request.user)
        try:
            cart=Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            print("Cart does not exist for the user.")
            cart=Cart.objects.create(user=request.user,cart_id=_cart_id(request))
            print('hi')
            cart.save()
            print(cart)
        try:
            cartitem=Cart_items.objects.get(medicine=medicine,cart=cart)
            print('no cart item')
            if medicine.stock > cartitem.quantity:
                cartitem.quantity +=1
            else:
                messages.error(request,'Already reached maximum quantity for {}!'.format(medicine.name))
                return redirect('cart:cart_detail')
        except Cart_items.DoesNotExist:
            cartitem=Cart_items.objects.create(
                medicine=medicine,
                cart=cart,
                quantity=1,
            )
        cartitem.save()
        print('end')
        return redirect('cart:cart_detail')

def cart_detail(request):
    if request.user.is_authenticated:
        cartitem=None;
        user=request.user
        print(request.user)
        try:
            cart=Cart.objects.get(user=user)
            print(user)
            cartitem=Cart_items.objects.filter(cart=cart,active=True)
        except ObjectDoesNotExist:
            pass
        return render(request,'cartdetail.html',dict(cartitems=cartitem,user=user))
    else:
        return redirect('login:login')


def delete_all(request,del_id):
    Cart_items.objects.get(id=del_id).delete()
    return redirect('cart:cart_detail')

def remove(request,cart_id,med_id):
    cartitem=Cart_items.objects.get(id=cart_id)
    if cartitem.quantity > 1:
        cartitem.quantity -=1
        cartitem.save()
    else :
        cartitem.delete()
    return redirect('cart:cart_detail')

def add_req(request,u_slug):

    try:
        user = CustomUser.objects.get(id=u_slug)
        cart = Cart.objects.get(user=user)
        print(cart)
        cartitems = Cart_items.objects.filter(cart=cart, active=True)

        print(cartitems)
        req = Req_items.objects.create(user=user)
        for cart_item in cartitems:
            req.cart_items.add(cart_item)
            medicine = Medicine.objects.get(name=cart_item)
            medicine.stock -=cart_item.quantity
            medicine.save()


        req.save()
        cartitems.update(cart=None)

    except ObjectDoesNotExist:
        pass
    return render(request,'success.html')

def request(request):
    if request.user.is_authenticated:
        req=Req_items.objects.all()
        print (req)
        return render(request,'request.html',{'req_items':req})
    else:
        return redirect('login:login')

def accept(request, req_id):
    if request.user.is_authenticated:
        print(req_id)
        try:
            reqitem = get_object_or_404(Req_items, id=req_id)
            reqitem.delete()
            return redirect('/')
        except Req_items.DoesNotExist:
            # Handle the case where the Req_items object does not exist
            return render(request, 'not_found_template.html')
    else:
        return redirect('login:login')

def decline(request,req_id):
    try:
        reqitem = get_object_or_404(Req_items, id=req_id)
        for cart_item in reqitem.cart_items.all():
            medicine=Medicine.objects.get(name=cart_item)
            medicine.stock +=cart_item.quantity
            medicine.save()

        reqitem.delete()
        return redirect('/')
    except Req_items.DoesNotExist:
        # Handle the case where the Req_items object does not exist
        return render(request, 'not_found_template.html')





