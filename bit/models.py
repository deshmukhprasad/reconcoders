from django.db import models

class login(models.Model):
	username = models.CharField(max_length=200)
	password = models.CharField(max_length = 200)
	def __str__(self):
		return self.username

class Patient(models.Model):		#model for patient
	patient_name = models.CharField(max_length = 200)
	patient_address = models.CharField(max_length = 200)
	bdate = models.DateField()
	patient_number = models.CharField(max_length=10)
	patient_gender = models.CharField(max_length=1)
	patient_username = models.CharField(max_length = 200)
	patient_pass = models.CharField(max_length = 200)
	def __str__(self):
		return self.patient_name

class Doctor(models.Model):			#model for doctor
	doctor_name = models.CharField(max_length = 200)
	doctor_address = models.CharField(max_length = 200)
	doctor_bdate = models.DateField()
	doctor_number = models.CharField(max_length=10)
	doctor_gender = models.CharField(max_length=1)
	qualification = models.CharField(max_length = 200)
	doctor_username = models.CharField(max_length=200)
	doctor_pass = models.CharField(max_length=200)
	def __str__(self):
	    return self.doctor_name

class Disease(models.Model):		#model for diseases
	patient = models.CharField(max_length = 200)
	doctor = models.CharField(max_length=200)
	symptoms_disease = models.CharField(max_length=200)
	disease_possible = models.CharField(max_length = 200)
	medicine = models.CharField(max_length=200)
	date = models.DateField()
	def __str__(self):
		return self.disease_possible

class BloodReport(models.Model): 
	patient_name = models.CharField(max_length=200)
	doctor_name = models.CharField(max_length = 200) 
	date = models.DateField()
	Report_Img = models.ImageField(upload_to='images/') 

