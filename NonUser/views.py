from django.shortcuts import render
from Donar.models import DonarModel
from Organization.models import OrganizationModel
from django.core.paginator import Paginator

def showIndex(request):
    og = OrganizationModel.objects.all()
    pg1 = Paginator(og,3)
    page1 = pg1.page(request.GET.get('page',1))
    data = DonarModel.objects.all()
    pg2 = Paginator(data,4)
    page2 = pg2.page(request.GET.get('page',1))
    return render(request,"index.html",{'donar':page2,'org':page1})

