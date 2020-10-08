from django.shortcuts import render,redirect
from Donar.models import DonarModel
from Organization.models import OrganizationModel
from django.core.paginator import Paginator
from NonUser.models import Nonuser

def showIndex(request):
    og = OrganizationModel.objects.filter(status="Confirm")
    pg1 = Paginator(og,3)
    page1 = pg1.page(request.GET.get('page',1))
    data = DonarModel.objects.all()
    pg2 = Paginator(data,4)
    page2 = pg2.page(request.GET.get('page',1))
    return render(request,"index.html",{'donar':page2,'org':page1})

def search_details(request):
    return render(request,"search_details.html")

def result(request):
    op = request.POST.get('option')
    bg = request.POST.get('bloodgroup')
    st = request.POST.get('state')
    cty = request.POST.get('city')
    if (op == "Donar" and cty):
        qs = DonarModel.objects.filter(state=st,city=cty,blood_group=bg)
        #print(qs)
        if qs:
            return render(request,"result.html",{'data':qs})
        else:
            return render(request, "result.html", {'msg':'Sorry! Donar is not avilable in your location'})
    elif (op == "Organization" and cty) :
        qs = OrganizationModel.objects.filter(state=st,city=cty)
        if qs:
            return render(request,"result.html",{'data':qs})
        else:
            return render(request, "result.html", {'msg':'Sorry! Organization is not avilable in your location'})
    else:
        return render(request, "result.html", {'msg': 'Please select all the Details'})

def nonuser_msg(request):
    nm = request.POST.get('name')
    email = request.POST.get('email')
    number = request.POST.get('number')
    message = request.POST.get('message')
    Nonuser(name=nm,email=email,cno=number,msg=message).save()
    return render(request,"index.html",{'msg':'Message is sent.You will get mail soon from admin'})