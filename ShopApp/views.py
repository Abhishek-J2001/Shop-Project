from django.shortcuts import render,redirect
from ShopApp.models import ShopDB,ProDB
from Frontend.models import ContactDB
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def indexpage(req):
    return render(req,"index.html")

def catpage(req):
    return render(req,"AddCategory.html")

def savedata(req):
    if req.method == "POST":
        cn = req.POST.get('cname')
        des = req.POST.get('description')
        img = req.FILES.get('image')
        obj = ShopDB(Cat_Name=cn, Description=des, Cat_Image=img)
        obj.save()
        return redirect(catpage)

def catdisplay(req):
    data = ShopDB.objects.all()
    return render(req, "CatDisplay.html", {'data': data})

def editpage(req,dataid):
    data = ShopDB.objects.get(id=dataid)
    return render(req,"EditCat.html", {'data': data})

def deletecat(request, dataid):
    cat = ShopDB.objects.filter(id=dataid)
    cat.delete()
    return redirect(catdisplay)

def updatedata(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('cname')
        des = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ShopDB.objects.get(id=dataid).Cat_Image
        ShopDB.objects.filter(id=dataid).update(Cat_Name=cn, Description=des, Cat_Image=file)
        return redirect(catdisplay)

def propage(req):
    category = ShopDB.objects.all()
    return render(req,"AddProduct.html",{'category':category})

def savedat(req):
    if req.method == "POST":
        cn = req.POST.get('cname')
        pn = req.POST.get('pname')
        des = req.POST.get('description')
        pri = req.POST.get('price')
        img = req.FILES.get('image')
        obj = ProDB(Cat_Name=cn,Pro_Name=pn, Description=des, Price=pri, Pro_Image=img)
        obj.save()
        return redirect(propage)

def prodisplay(req):
    data = ProDB.objects.all()
    return render(req, "ProDisplay.html", {'data': data})

def editpag(req,dataid):
    data = ProDB.objects.get(id=dataid)
    cat = ShopDB.objects.all()
    return render(req,"EditPro.html", {'data': data,'cat':cat})

def deletepro(request, dataid):
    pro = ProDB.objects.filter(id=dataid)
    pro.delete()
    return redirect(prodisplay)

def updatedat(request, dataid):
    if request.method == "POST":
        cn = request.POST.get('cname')
        pn = request.POST.get('pname')
        des = request.POST.get('description')
        pri = request.POST.get('price')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = ProDB.objects.get(id=dataid).Pro_Image
        ProDB.objects.filter(id=dataid).update(Cat_Name=cn,Pro_Name=pn, Description=des, Price=pri, Pro_Image=file)
        return redirect(prodisplay)

def admin_login(req):
    return render(req,"AdminLogin.html")

def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pwd)
            if user is not None:
                login(request,user)
                request.session['username'] = un
                request.session['password'] = pwd
                return redirect(indexpage)
            else:
                return redirect(adminlogin)
        else:
            return redirect(admin_login)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)

def displaycontact(request):
    data = ContactDB.objects.all()
    return render(request,"ContactDisplay.html", {'data':data})

def deletecon(request, dataid):
    pro = ContactDB.objects.filter(id=dataid)
    pro.delete()
    return redirect(displaycontact)