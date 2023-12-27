from django.contrib.auth import get_user_model
from django.db import models
from firstaid_app.models import Medicine

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    cart_id=models.CharField(unique=True,max_length=250)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.cart_id

class Cart_items(models.Model):
    medicine=models.ForeignKey(Medicine,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.medicine.name

class Req_items(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    cart_items = models.ManyToManyField(Cart_items)




