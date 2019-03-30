from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from bit.forms import Loginform, Diseaseform,  Patientform, Doctorform, Bloodform
from .geo import foo
from bit.models import Doctor, Disease, Patient, BloodReport
from .dp import chart1
from .dp import chart2
from django.http import HttpResponse
from django.shortcuts import render


def login(request):
    if request.method == 'POST':
        form = Loginform(request.POST or None)
        if form.is_valid():
            form.save()
            # messages.success(request,('List has been updated'))
            user = form.cleaned_data['username']
            passw = form.cleaned_data['password']
            try:
                all_items = Doctor.objects.get(doctor_username=user)
                named = all_items.doctor_name
                request.session['dname'] = named
                info = Disease.objects.filter(doctor=named)
                # print(info)
                # all_items = go

                return render(request, "doctordash.html", {'all_items': all_items,'info':info})
            except ObjectDoesNotExist:
                go = None
                try:
                    pat = Patient.objects.get(patient_username=user)
                    all_items = pat
                    infop = Disease.objects.filter(patient=all_items.patient_name)
                    print(infop)
                    return render(request, "patientdash.html", {'all_items': all_items,'infop':infop})
                except ObjectDoesNotExist:
                    pat = None
            #return render(request, "login.html", {'form': form})
    return render(request, "login.html", {})




def patient(request):
    if request.method == 'POST':
        form = Patientform(request.POST or None)
        if form.is_valid():
            form.save()
            user = request.session['dname']
            patientlist = Patient.objects.all()
            return render(request, "disease.html", {'patientlist':patientlist,'doctor_name': user})
    return render(request, "patient.html", {})


def doctor(request):
    if request.method == 'POST':
        form = Doctorform(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, "login.html", {})
    return render(request,"doctor.html",{})

def patientdash(request):
    return render(request,"patientdash.html",{})

def doctordash(request):
    if (request.GET.get('mybtn')):
        user =request.session['dname']
        print(user)
        patientlist = Patient.objects.all()
        return render(request,"disease.html", {'patientlist':patientlist,'doctor_name':user})


def disease(request):
    if request.method == 'POST':
        patientlist = Patient.objects.all()
        form = Diseaseform(request.POST or None)
        if form.is_valid():
            dname = form.cleaned_data['doctor']
            form.save()
            user = request.session['dname']
            all_items = Doctor.objects.get(doctor_username=user)
            named=all_items.doctor_name
            info=Disease.objects.filter(doctor=named)
            return render(request,"doctordash.html",{'all_items': all_items,'info':info})
    return render(request,"disease.html",{})

def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    # sd is selected disease

    a = Disease.objects.all()
    n = len(a)
    s = a[n - 1].date
    s=str(s)
    m = int(s[5:7])
    y = int(s[:4])
    add =[]
    dis=[]
    for i in range(len(a)):
        dis.append(a[i].disease_possible)

    dis=list(set(dis))
    if(request.method=='POST'):
        for i in a:
            #s1=a.date
            m1 = int(s[5:7])
            y1 = int(s[:4])
            sd=request.POST.get('p')
            print(sd)
            if  y==y1:
                if m==m1:
                    if sd==i.disease_possible:
                    	print('ghusla')
                    	pat=i.patient
                    	print(pat)
                    	k=Patient.objects.filter(patient_name=pat)
                    	add.append(k[0].patient_address)

        co=foo(add)
        return render(request, 'default.html',{ 'mapbox_access_token': mapbox_access_token,'co':co,'dis':dis})
    return render(request, 'default.html', {'mapbox_access_token': mapbox_access_token,'dis':dis})


def home1(request):
    #chart1()
    z,d=chart1()
    dis=Disease.objects.all()
    if(request.method=='POST'):
        j=request.POST.get('p')
        c=request.POST.get('p')
        print(c)
        z,d=chart1()
        print(z)
        i=d.index(str(c))
        k=z[i]
        return render(request,'index1.html',{'n':k,'d':d})
    return render(request,'index1.html',{'d':d})



def home2(request):
    c,d=chart2()
    return render(request,'index2.html',{'c':c,'d':d})


def home3(request):
    #medicine selected=j
    #year selected=b
    di=Disease.objects.all()
    dis=[]
    ye=[]
    for _ in range(len(di)):
        dis.append(di[_].medicine)

    for _ in range(len(di)):
        s=di[_].date
        s=str(s)
        year=int(s[:4])
        ye.append(year)

    d={}
    q=[]
    if(request.method=='POST'):
        j=request.POST.get('p')
        b=int(request.POST.get('p1'))
        print(j,b)
        a=Disease.objects.filter(medicine=j)
        for i in a:
            s=str(i.date)
            y=int(s[:4])
            print(y)
            print(b)
            if y==b:
                print('ghusla')
                doc=i.doctor
                print(doc)
                f=Doctor.objects.filter(doctor_name=doc)
                add=f[0].doctor_address
                if add in list(d.keys()):
                    d[add]+=1
                else:
                    d[add]=1
        adder=list(d.keys())
        for i in adder:
            q.append(d[i])
        print(adder)
        print(q)
        return render(request,'index3.html',{'add':adder,'q':q,'dis':dis,'ye':ye})
    return render(request,'index3.html',{'dis':dis,'ye':ye})

def blood(request): 
    if request.method == 'POST': 
        form = Bloodform(request.POST, request.FILES) 
  
        if form.is_valid(): 
            form.save() 
            return Redirect('success') 
    else: 
        form = Bloodform() 
    return render(request, 'blood.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded') 

def display_hotel_images(request): 
  
    if request.method == 'GET': 
  
        # getting all the objects of hotel. 
        Hotels = Hotel.objects.all()  
        return render(request, 'display_hotel_images.html', {'hotel_images' : Hotels}) 