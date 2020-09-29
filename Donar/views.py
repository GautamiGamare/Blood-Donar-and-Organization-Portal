from django.shortcuts import render,redirect
from Donar.models import DonarModel
from Donar.DonarForm import DonarForm
from django.db.models import Q

def donar_login(request):
    return render(request,"donar/index.html")

def donar_registration(req):
    return render(req,"donar/donar_registration.html",{'form':DonarForm()})

def validate_donar(request):
    em = request.POST.get('email')
    ps = request.POST.get('pass')
    print(em,ps)
    try:
        qs = DonarModel.objects.get(Q(email=em,password=ps))
        request.session['donar_id'] = qs.id
        return render(request,"donar/donar_welcome.html")
    except DonarModel.DoesNotExist:
        messages = "Invalid Username and Password"
        return render(request,"donar/index.html",{'msg':messages})


def save_donar(request):
    nm = request.POST.get('name')
    cn1 = request.POST.get('c1')
    cn2 = request.POST.get('c2')
    bgp = request.POST.get('bg')
    dt = request.POST.get('date')
    st= request.POST.get('state')
    ct = request.POST.get('city')
    ar = request.POST.get('area')
    em = request.POST.get('email')
    ps = request.POST.get('pass')
    ph = request.FILES['photo']
    print(nm,cn1,cn2,bgp,dt,st,ct,ar,em,ps,ph)
    DonarModel(name=nm,contact_number=cn1,contact_number_2=cn2,blood_group=bgp,last_donation_date=dt,
               state=st,city=ct,area=ar,email=em,password=ps,photo=ph).save()
    messages = "Registration Successful"
    return render(request,"donar/index.html",{'msg':messages})