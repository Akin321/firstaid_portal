from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    is_administrator=models.BooleanField(default=False)


    # groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    # user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

# class AdminUser(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
#
#     def save(self, *args, **kwargs):
#         admin_group, created = Group.objects.get_or_create(name='Admins')
#         self.user.groups.add(admin_group)
#
#         admin_permissions = Permission.objects.all()
#         self.user.user_permissions.set(admin_permissions)
#
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.user.username

