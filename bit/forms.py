from django import forms

from .models import login
from .models import Patient
from .models import Doctor
from .models import Disease
from .models import BloodReport

class Loginform(forms.ModelForm):
    class Meta:
        model = login
        fields = ["username", "password"]

class Patientform(forms.ModelForm):
	class Meta:
		model = Patient
		exclude = ()

class Doctorform(forms.ModelForm):
	class Meta:
		model = Doctor
		exclude = ()

class Diseaseform(forms.ModelForm):
	class Meta:
		model = Disease
		exclude = ()

  
class Bloodform(forms.ModelForm):   
    class Meta: 
        model = BloodReport 
        exclude = () 