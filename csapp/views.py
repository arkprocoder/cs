from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from .models import Contact
# Create your views here.
def index(request):
    if request.method=="POST":
        Name=request.POST.get('name','')
        Emailaddress=request.POST.get('emailaddress','')
        Address=request.POST.get('address','')
        Location=request.POST.get('location','')
        Universityname=request.POST.get('Universityname','')      
        contact=Contact(Name=Name,Emailaddress=Emailaddress,Address=Address,Location=Location,Universityname=Universityname)
        contact.save()      
        return HttpResponse("Success")
    return render(request,'index.html')
           
        
    
           



   
