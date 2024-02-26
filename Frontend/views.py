from django.shortcuts import render,redirect
from ShopApp.models import ShopDB,ProDB
from Frontend.models import ContactDB,RegisterDB

# Create your views here.
def homepage(req):
    cat = ShopDB.objects.all()
    return render(req,"Home.html", {'cat':cat})

def propage(req):
    pro = ProDB.objects.all()
    return render(req,"Product.html",{'pro':pro})

def singlepage(req,proid):
    data = ProDB.objects.get(id=proid)
    return render(req,"singleproduct.html", {'data':data})

def procatpage(request,cat_name):
    data = ProDB.objects.filter(Cat_Name=cat_name)
    return render(request,"procatdisplay.html",{'data':data})

def serpage(request):
    return render(request,"Service.html")

def aboutpage(request):
    return render(request,"About.html")

def conpage(request):
    return render(request,"Contact.html")

def savecon(request):
    if request.method == "POST":
        n = request.POST.get('name')
        e = request.POST.get('email')
        m = request.POST.get('number')
        msg = request.POST.get('msg')
        obj = ContactDB(Name=n, Email=e, Mobile=m, Message=msg)
        obj.save()
        return redirect(conpage)

def regpage(request):
    return render(request,"Register.html")

def savereg(request):
    if request.method=="POST":
        na = request.POST.get('name')
        em = request.POST.get('email')
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        obj = RegisterDB(Name=na, Email=em, Username=un, Password=pwd)
        obj.save()
        return redirect(login_page)

def login_page(request):
    return render(request,"Login.html")

def user_login(request):
    if request.method=="POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if RegisterDB.objects.filter(Username=un, Password=pwd).exists():
            request.session['Username'] = un
            request.session['Password'] = pwd
            return redirect(homepage)
        else:
            return redirect(login_page)
    else:
        return redirect(login_page)

def user_logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(login_page)