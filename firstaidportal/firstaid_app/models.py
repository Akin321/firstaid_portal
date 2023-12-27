from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=150,unique=True)
    desc=models.TextField()

    class Meta:
        ordering=('name',)

    def save(self, *args, **kwargs):
        # Automatically generate a slug when saving the instance
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('firstaid_app:view_by_cat',args=[self.slug])

    def __str__(self):
        return self.name;
class Medicine(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    stock=models.IntegerField()
    exp_date=models.DateField()
    created=models.DateTimeField(auto_now_add=True)
    available=models.BooleanField(default=True)
    img=models.ImageField(upload_to='medicine')
    desc = models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)


    def save(self, *args, **kwargs):
        # Automatically generate a slug when saving the instance
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('firstaid_app:view_med',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)

    def __str__(self):
        return self.name;
