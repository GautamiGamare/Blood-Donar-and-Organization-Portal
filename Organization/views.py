from django.shortcuts import render
from Organization.models import OrganizationModel

def login(request):
    return render(request,"organization/org_login.html")

def org_registration(request):
    return render(request,"organization/org_registration.html")

def save_org(request):
    nm = request.POST.get('name')
    ty = request.POST.get('type')
    cn1 = request.POST.get('c1')
    cn2 = request.POST.get('c2')
    state = request.POST.get('state')
    city =request.POST.get('city')
    area = request.POST.get('area')
    email =request.POST.get('email')
    ph = request.FILES['photo']
    OrganizationModel(name=nm,type=ty,contact_number=cn1,contact_number_2=cn2,
                      state=state,city=city,area=area,email=email,photo=ph).save()
    return render(request,"organization/org_login.html",{'msg':'Thank you for Registering..You will get uswename and password by Email'})

def validate_org(request):
    pass

