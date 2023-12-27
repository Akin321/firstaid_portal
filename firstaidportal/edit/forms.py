from django import forms
from firstaid_app.models import Medicine,Category
class MedForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields=['name','stock','exp_date','img','desc','category']

class CatForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name','desc']