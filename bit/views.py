from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from .geo import foo, months
from bit.forms import Loginform
from bit.models import Doctor, Disease, Patient
from .dp import chart1
from .dp import chart2
from .dp import chart3


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
    return render(request,"patient.html",{})


def doctor(request):
    return render(request,"doctor.html",{})

def patientdash(request):
    return render(request,"patientdash.html",{})

def doctordash(request):
    return render(request,"doctordash.html",{})

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
                        doc=i.doctor
                        f=Doctor.objects.filter(doctor_name=doc)
                        if f[0].doctor_address not in add:
                            add.append(f[0].doctor_address)
        co=foo(add)
        return render(request, 'default.html',{ 'mapbox_access_token': mapbox_access_token,'co':co,'dis':dis})
    return render(request, 'default.html', {'mapbox_access_token': mapbox_access_token, 'co': co,'dis':dis})


def home1(request):
    chart1()
    dis=Disease.objects.all()
    d=[]
    print(request.POST.get('p'))
    for i in range(len(dis)):
        d.append(dis[i].disease_possible)
    z=chart1()
    print('hello')
    return render(request,'index1.html',{'d':d})


def home2(request):
    c,d=chart2()
    return render(request,'index2.html',{'c':c,'d':d})


def home3(request):
    chart3()
    return render(request,'index3.html',{})

