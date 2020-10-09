from django.shortcuts import render,redirect
from Donar.models import DonarModel
from Donar.DonarForm import DonarForm
from django.db.models import Q
from passlib.hash import pbkdf2_sha256
from Admin.models import adminModel
from Admin.models import chatInfo
from django.contrib import messages



def donar_login(request):
    return render(request,"donar/index.html")

def donar_registration(req):
    return render(req,"donar/donar_registration.html",{'form':DonarForm()})

def validate_donar(request):
    em = request.POST.get('email')
    ps = request.POST.get('pass')
    try:
        qs = DonarModel.objects.get(Q(email=em))
        pbkdf2_sha256.verify(ps, qs.password)
        request.session['donar_id'] = qs.id
        id = request.session['donar_id']
        receiver = DonarModel.objects.get(id=id)
        msg = chatInfo.objects.filter(receiver=receiver.email,status="Pending")
        if msg:
            for x in msg:
                if x.sender_name == x.sender:
                    return render(request, "donar/donar_welcome.html",
                                  {'donar': DonarModel.objects.all().exclude(id=id),
                     'admin': adminModel.objects.all(),'admin_msg': msg,'active_donar':DonarModel.objects.get(id=id)})
                elif x.sender_name != x.sender:
                    return render(request, "donar/donar_welcome.html",
                                  {'donar': DonarModel.objects.all().exclude(id=id),
                                   'admin': adminModel.objects.all(),
                                   'donar_msg': msg,
                                   'active_donar':DonarModel.objects.get(id=id)})
        else:
            return render(request, "donar/donar_welcome.html", {'donar': DonarModel.objects.all().exclude(id=id),
                                                                'admin': adminModel.objects.all(),
                                                                'active_donar':DonarModel.objects.get(id=id)})

    except DonarModel.DoesNotExist:
        messages = "Invalid Username and Password"
        return render(request,"donar/index.html",{'msg':messages})


def donar_welcome(request):
    id =request.session['donar_id']
    receiver = DonarModel.objects.get(id=id)
    msg = chatInfo.objects.filter(receiver=receiver.email,status="Pending")
    if msg:
        for x in msg:
            if x.sender_name == x.sender:
                return render(request, "donar/donar_welcome.html",
                              {'donar': DonarModel.objects.all().exclude(id=id), 'admin': adminModel.objects.all(), 'admin_msg': msg, 'active_donar': DonarModel.objects.get(id=id)})
            else:
                return render(request, "donar/donar_welcome.html",
                              {'donar': DonarModel.objects.all().exclude(id=id), 'admin': adminModel.objects.all(), 'donar_msg': msg, 'active_donar': DonarModel.objects.get(id=id)})
    else:
        return render(request, "donar/donar_welcome.html", {'donar': DonarModel.objects.all().exclude(id=id), 'admin': adminModel.objects.all(), 'active_donar': DonarModel.objects.get(id=id)})

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

    encrpt_password = pbkdf2_sha256.encrypt(ps,rounds=12000,salt_size=32)

    DonarModel(name=nm,contact_number=cn1,contact_number_2=cn2,blood_group=bgp,last_donation_date=dt,
               state=st,city=ct,area=ar,email=em,password=encrpt_password,photo=ph).save()
    messages.success(request,"Registration Successful")
    return redirect('donar_welcome')

def show_msg(request):
    num = request.GET.get('no')
    id = request.session['donar_id']
    receiver1 = DonarModel.objects.get(id=id)
    msg = chatInfo.objects.filter(receiver=receiver1.email, status="Pending")
    if msg:
        for x in msg:
            if x.sender_name == x.sender:
                return render(request, "donar/show_msg.html",
                              {'chat':chatInfo.objects.filter(id=num),'donar': DonarModel.objects.all().exclude(id=id),
                               'admin': adminModel.objects.all(), 'admin_msg': msg, 'active_donar': DonarModel.objects.get(id=id)})
            else:
                return render(request, "donar/show_msg.html",
                              {'chat':chatInfo.objects.filter(id=num),'donar': DonarModel.objects.all().exclude(id=id),
                               'admin': adminModel.objects.all(), 'donar_msg': msg, 'active_donar': DonarModel.objects.get(id=id)})
    else:
        return render(request, "donar/show_msg.html",
                      {'chat':chatInfo.objects.filter(id=num),'donar': DonarModel.objects.all().exclude(id=id),
                       'admin': adminModel.objects.all(), 'active_donar': DonarModel.objects.get(id=id)})

def msg_donar(request):
    num=request.GET.get('no')
    id = request.session['donar_id']
    receiver = DonarModel.objects.get(id=id)
    msg = chatInfo.objects.filter(receiver=receiver.email, status="Pending")
    if msg:
        for x in msg:
            if x.sender_name == x.sender:
                return render(request, "donar/msg_donar.html",
                              {'donar1':DonarModel.objects.filter(id=num),'donar': DonarModel.objects.all().exclude(id=id),
                               'admin': adminModel.objects.all(), 'admin_msg': msg, 'active_donar': DonarModel.objects.get(id=id)})
            else:
                return render(request, "donar/msg_donar.html",
                              {'donar1':DonarModel.objects.filter(id=num),'donar': DonarModel.objects.all().exclude(id=id),
                               'admin': adminModel.objects.all(), 'donar_msg': msg, 'active_donar': DonarModel.objects.get(id=id)})
    else:
        return render(request, "donar/msg_donar.html", {'donar1':DonarModel.objects.filter(id=num),'donar': DonarModel.objects.all().exclude(id=id),
                            'admin': adminModel.objects.all(), 'active_donar': DonarModel.objects.get(id=id)})

def msg_admin(request):
    num = request.GET.get('no')
    data1 = adminModel.objects.filter(id=num)

    id = request.session['donar_id']
    data = DonarModel.objects.all().exclude(id=id)
    admin = adminModel.objects.all()
    # --
    receiver = DonarModel.objects.get(id=id)
    msg = chatInfo.objects.filter(receiver=receiver.email, status="Pending")
    id = request.session['donar_id']
    login_donar = DonarModel.objects.get(id=id)
    if msg:
        for x in msg:
            if x.sender_name == x.sender:
                return render(request, "donar/msg_admin.html",
                              {'admin1': data1, 'donar': data, 'admin': admin, 'admin_msg': msg,
                               'active_donar': login_donar})
            else:
                return render(request, "donar/msg_admin.html",
                              {'admin1': data1, 'donar': data, 'admin': admin, 'donar_msg': msg,
                               'active_donar': login_donar})
    else:
        return render(request, "donar/msg_admin.html",
                      {'admin1': data1, 'donar': data, 'admin': admin, 'active_donar': login_donar})

def save_donar_msg1(request):
    id = request.session['donar_id']
    data = DonarModel.objects.get(id=id)
    chatInfo(sender=data.email, receiver=request.POST.get('uname'),
             message=request.POST.get('msg'),sender_name=data.name,receiver_name=request.POST.get('name')).save()
    messages.success(request,"Message is sent !!")
    return redirect('donar_welcome')

def save_admin_msg1(request):
    id = request.session['donar_id']
    data = DonarModel.objects.get(id=id)
    chatInfo(sender=data.email, receiver=request.POST.get('uname'),
             message=request.POST.get('msg'),sender_name=data.name,receiver_name=request.POST.get('uname')).save()
    messages.success(request, "Message is sent !!")
    return redirect('donar_welcome')

def make_msg_read(request):
    id = request.GET.get('no')
    print(id)
    data = chatInfo.objects.get(id=id)
    data.status = "Read"
    data.save()
    messages.success(request, "Message is marked as read")
    return redirect('donar_welcome')

def reply_msg(request):
    id = request.session['donar_id']
    data = DonarModel.objects.get(id=id)
    receiver = request.POST.get('receiver')
    receiver_nm = request.POST.get('receiver_name')
    chatInfo(sender=data.email, receiver=receiver,
             message=request.POST.get('msg'), sender_name=data.name,
             receiver_name=receiver_nm).save()
    msg_id = chatInfo.objects.get(id=request.POST.get('id'))
    msg_id.status = "Read"
    msg_id.save()
    messages.success(request, "Message is sent !!")
    data1 = DonarModel.objects.all().exclude(id=id)
    admin = adminModel.objects.all()
    #--
    receiver1 = DonarModel.objects.get(id=id)
    msg = chatInfo.objects.filter(receiver=receiver1.email,status="Pending")
    login_donar = DonarModel.objects.get(id=id)
    if msg:
        for x in msg:
            if x.sender_name == x.sender:
                return render(request, "donar/donar_welcome.html",
                              {'donar': data1, 'admin': admin, 'admin_msg': msg, 'active_donar': login_donar})
            else:
                return render(request, "donar/donar_welcome.html",
                              {'donar': data1, 'admin': admin, 'donar_msg': msg, 'active_donar': login_donar})
    else:
        return render(request, "donar/donar_welcome.html", {'donar': data1, 'admin': admin, 'active_donar': login_donar})




def donar_logout(request):
    del request.session['donar_id']
    return redirect("donar_login")
