from django.shortcuts import render, redirect
from Organization.models import OrganizationModel
from django.db.models import Q
from passlib.hash import pbkdf2_sha256
from Admin.models import adminModel,chatInfo

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

def admin_message(request):
    id = request.session['org_id']
    data = OrganizationModel.objects.get(id=id)
    chat = chatInfo.objects.filter(receiver=data.email, status="Pending")
    return chat

def validate_org(request):
    em = request.POST.get('email')
    ps = request.POST.get('pass') #PUN1@1234Mah PUN2@1234Mah
    try:
        qs = OrganizationModel.objects.get(Q(email=em))
        pbkdf2_sha256.verify(ps, qs.password)
        request.session['org_id'] = qs.id
        x=admin_message(request)
        return render(request, "Organization/organization_welcome.html",{'admin':adminModel.objects.all(),'admin_msg':x})
    except OrganizationModel.DoesNotExist:
        messages = "Invalid Username and Password"
        return render(request, "Organization/org_login.html", {'msg': messages})

def welcome_org(request):
    x = admin_message(request)
    return render(request, "Organization/organization_welcome.html",{'admin':adminModel.objects.all(),'admin_msg':x})

def check_admin_msg(request):
    x = admin_message(request)
    id = request.GET.get('no')
    data = chatInfo.objects.get(id=id)
    return render(request,"Organization/check_admin_msg.html",{'admin':adminModel.objects.all(),'admin_msg':x,'chat':data})

def reply_message1(request):
    id = request.session['org_id']
    data = OrganizationModel.objects.get(id=id)
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

def msg_read1(request):
    pass

def send_msg_admin(request):
    pass

def org_logout(req):
    del req.session['org_id']
    return redirect('login_org')