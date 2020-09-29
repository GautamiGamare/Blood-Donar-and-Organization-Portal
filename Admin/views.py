from django.core.mail import send_mail
from BloodPortal import settings as se
from django.shortcuts import render
from Admin.models import adminModel
from django.views.generic import ListView
from Donar.models import DonarModel
from Organization.models import OrganizationModel
from django.http import HttpResponse

def validate_login(request):
    try:
        res = adminModel.objects.get(username = request.POST.get('uname'),password=request.POST.get('pass'))
        return render(request,"admin/welcome_admin.html",{'name':res.username})
    except adminModel.DoesNotExist:
        return render(request,"admin/login.html",{'msg':'Invalid Username or Password'})

def donar_details(request):
    return render(request,"admin/donar_details.html",{'data':DonarModel.objects.all()})

def org_details(request):
    pending= OrganizationModel.objects.filter(status="Pending")
    confirm = OrganizationModel.objects.filter(status="Confirm")
    return render(request, "admin/org_details.html",{'data':pending,'conf':confirm})

def give_access(request):
    id =request.GET.get('no')
    res = OrganizationModel.objects.get(id=id)
    res.status = "Confirm"
    res.password = res.city[0:3]+str(res.id)+"@1234"+res.state[0:3]
    res.uname = res.email
    res.save()
    send_mail("Confirmation mail from RED-ROSS", "Thank you for registering and being part of RED-ROSS Blood Portal\n Your Username is "+res.uname+
              " And Password is "+res.password +"\n best wishes from RED-ROSS" ,
              se.EMAIL_HOST_USER, [res.email],
              fail_silently=False)
    return render(request, "admin/org_details.html",{'msg':'Access is given','data': OrganizationModel.objects.filter(status="Pending"),'conf':OrganizationModel.objects.filter(status="Confirm")})


