from django.core.mail import send_mail
from BloodPortal import settings as se
from django.shortcuts import render, redirect
from Donar.models import DonarModel
from Organization.models import OrganizationModel
from NonUser.models import Nonuser
from passlib.hash import pbkdf2_sha256
from Admin.models import adminModel,chatInfo
from django.db.models import Q
from django.contrib import messages

def donar_msg(request):
    id = request.session['admin_id']
    data = adminModel.objects.get(id=id)
    chat = chatInfo.objects.filter(receiver_name=data.username,status = "Pending")
    return chat


def validate_login(request):
    try:
        un = request.POST.get('uname')
        data = adminModel.objects.get(Q(username=un))
        request.session['admin_id'] = data.id
        nonuser = Nonuser.objects.filter(status='Pending')
        x= donar_msg(request)
        return render(request,"admin/admin_wlcm.html",{'nonuser':nonuser,
                                                       'donar':DonarModel.objects.all(),
                                                       'org':OrganizationModel.objects.all(),
                                                       'donar_msg':x},)
    except adminModel.DoesNotExist:
        return render(request,"admin/login.html",{'msg':'Invalid Username or Password'})

def welcome_admin(request):
    x = donar_msg(request)
    return render(request,"admin/admin_wlcm.html",{'nonuser':Nonuser.objects.filter(status='Pending'),
                     'donar':DonarModel.objects.all(),'org':OrganizationModel.objects.all(),'donar_msg':x})

def donar_details(request):
    x = donar_msg(request)
    nonuser = Nonuser.objects.filter(status='Pending')
    return render(request,"admin/donar_details.html",{'donar':DonarModel.objects.all(),
                    'nonuser':nonuser,'org':OrganizationModel.objects.all(),'donar_msg':x})

def org_details(request):
    x = donar_msg(request)
    pending= OrganizationModel.objects.filter(status="Pending")
    confirm = OrganizationModel.objects.filter(status="Confirm")
    return render(request, "admin/org_details.html",{'pend':pending,'conf':confirm,
                                                     'donar':DonarModel.objects.all(),
                                                     'nonuser':Nonuser.objects.filter(status='Pending'),
                                                     'org':OrganizationModel.objects.all(),
                                                     'donar_msg':x})

def give_access(request):
    id =request.GET.get('no')
    res = OrganizationModel.objects.get(id=id)
    res.status = "Confirm"
    password = res.city[0:3]+str(res.id)+"@1234"+res.state[0:3]
    res.uname = res.email
    res.password = pbkdf2_sha256.hash(password)
    res.save()
    send_mail("Confirmation mail from RED-ROSS", "Thank you for registering and being part of RED-ROSS Blood Portal\n Your Username is "+res.uname+
              " And Password is "+password +"\n best wishes from RED-ROSS" ,
              se.EMAIL_HOST_USER, [res.email],
              fail_silently=False)
    return render(request, "admin/org_details.html",{'msg':'Access is given',
                                                     'pend': OrganizationModel.objects.filter(status="Pending"),
                                                     'conf':OrganizationModel.objects.filter(status="Confirm"),
                                                     'donar': DonarModel.objects.all(),
                                                     'nonuser': Nonuser.objects.filter(status='Pending'),
                                                     'org': OrganizationModel.objects.all()
                                                     })

#------------------------------------------

def nonuser_msg_display(request):
    idnum = request.GET.get('no')
    res = Nonuser.objects.filter(id=idnum)
    x = donar_msg(request)
    return render(request,"admin/nonuser_msg.html",{'data':res,'nonuser':Nonuser.objects.filter(status='Pending'),
                     'donar':DonarModel.objects.all(),'org':OrganizationModel.objects.all(),
                                                    'donar_msg':x})

def msg_display(request):
    x = donar_msg(request)
    idnum = request.GET.get('no')
    chat = chatInfo.objects.get(id=idnum)
    return render(request,"admin/donar_msg_display.html",{'chat':chat,'nonuser':Nonuser.objects.filter(status='Pending'),
                     'donar':DonarModel.objects.all(),'org':OrganizationModel.objects.all(),
                                                    'donar_msg':x})

def reply_message(request):
    id = request.session['admin_id']
    data = adminModel.objects.get(id=id)
    receiver = request.POST.get('receiver')
    receiver_nm = request.POST.get('receiver_name')
    chatInfo(sender=data.username, receiver=receiver,
             message=request.POST.get('msg'), sender_name=data.username,
             receiver_name=receiver_nm).save()
    msg_id = chatInfo.objects.get(id=request.POST.get('id'))
    msg_id.status = "Read"
    msg_id.save()
    messages.success(request, "Message is sent !!")
    return redirect('welcome_admin')

def msg_read(request):
    id = request.GET.get('no')
    data = chatInfo.objects.get(id=id)
    data.status = "Read"
    data.save()
    messages.success(request, "Message is marked as read")
    return redirect('welcome_admin')

def send_nonuser_email(request):
    reply = request.POST.get('msg')
    email = request.POST.get('mail')
    send_mail("From Red-Ross Team",reply,se.EMAIL_HOST_USER,[email],
              fail_silently=False)
    idnum = request.POST.get('no')
    res = Nonuser.objects.get(id=idnum)
    res.status = 'Sent'
    res.save()
    nonuser = Nonuser.objects.filter(status='Pending')
    messages.success(request,"Email is sent successfully!!")
    return redirect('welcome_admin')

def send_msg_donar(request):
    idnum = request.GET.get('no')
    data = DonarModel.objects.filter(id=idnum)
    return render(request,"admin/send_msg_donar.html",{'data':data,'nonuser':Nonuser.objects.filter(status='Pending'),
                     'donar':DonarModel.objects.all(),'org':OrganizationModel.objects.all()})

def send_msg_org(request):
    idnum = request.GET.get('no')
    data = OrganizationModel.objects.filter(id=idnum)
    return render(request, "admin/send_msg_org.html", {'data': data,'nonuser':Nonuser.objects.filter(status='Pending'),
                     'donar':DonarModel.objects.all(),'org':OrganizationModel.objects.all()})

def save_donar_msg(request):
    id = request.session['admin_id']
    data = adminModel.objects.get(id=id)
    chatInfo(sender=data.username, receiver=request.POST.get('uname'),
             message=request.POST.get('msg'),
             sender_name=data.username,
             receiver_name=request.POST.get('name')).save()
    messages.success(request, "Message is sent !!")
    return redirect('welcome_admin')

def save_org_msg(request):
    id = request.session['admin_id']
    data = adminModel.objects.get(id=id)
    chatInfo(sender=data.username,receiver=request.POST.get('uname'),
             message=request.POST.get('msg'),
             sender_name=data.username,
             receiver_name=request.POST.get('name')).save()
    messages.success(request, "Message is sent !!")
    return redirect('welcome_admin')

def logout(request):
    del request.session['admin_id']
    return redirect("login")
