from django.contrib import admin
from . models import Category,Medicine
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class MedicineAdmin(admin.ModelAdmin):
    list_display = ['name','stock','available','exp_date','created']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['stock','available']
admin.site.register(Medicine,MedicineAdmin)
