from django.shortcuts import render,redirect,HttpResponse
from .models import signupUser,product,usercart
from math import ceil
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

allProds=[]
catprods=product.objects.values('product_category','id')
cats={item['product_category'] for item in catprods}
for cat in cats:
    prod=product.objects.filter(product_category=cat)
    n=len(prod)
    nSlides=n//4 + ceil((n/4)-(n//4))
    allProds.append([prod,range(1,nSlides),nSlides])

def index(request):
    allProds=[]
    catprods=product.objects.values('product_category','id')
    cats={item['product_category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(product_category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    productcount=usercart.objects.filter(cusername=request.user).count()
    params={'allProds':allProds,'pcount':productcount}
    return render(request,"index.html",params)

def home(request):
    return render(request,"index.html")

def mycart(request):
    if request.method=="POST":
        pid=request.POST.get('prodid')
        psize=request.POST.get('psize')
        usname=request.POST.get('uname')
        pname=request.POST.get('prodname')
        pprice=request.POST.get('prodprice')
        pdesc=request.POST.get('proddesc')
        pcat=request.POST.get('pcat')
        uc=usercart.objects.filter(cusername=request.user)
        c=0
        for i in uc.iterator():
            if pname==(i.cproduct_name):
                c=1
        if c==0:
            b=usercart(cprod_id=pid,cprod_size=psize,cproduct_cat=pcat,cusername=usname,cproduct_name=pname,cproduct_price=pprice,cproduct_desc=pdesc)
            b.save()  
            messages.success(request," "+pname+" added to cart")
        else:
            messages.error(request," "+pname+" already in the cart")   
    return HttpResponse("received")

def usercarts(request):
    allProds=[]
    catprods=product.objects.values('product_category','id')
    cats={item['product_category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(product_category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    ucart=usercart.objects.all()
    loguser=usercart.objects.filter(cusername=request.user)
    productcount=usercart.objects.filter(cusername=request.user).count()
    params={'allProds':allProds,'ucart':ucart,'loguser':loguser,'pcount':productcount}
    return render(request,"usercart.html",params)

def myproducts(request):
    allProds=[]
    catprods=product.objects.values('product_category','id')
    cats={item['product_category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(product_category=cat)
        n=len(prod)
        nSlides=n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
    uproducts=product.objects.filter(product_uname=request.user)
    productcount=usercart.objects.filter(cusername=request.user).count()
    params={'allProds':allProds,'uproducts':uproducts,'pcount':productcount}
    return render(request,"myproducts.html",params)

def removefromcart(request):
    if request.method=="POST":
        loguser=request.POST.get('loguser')
        pid=request.POST.get('pid')
        pname=request.POST.get('pname')
        print(pname)
        qc=usercart.objects.filter(cusername=loguser)
        print("before "+str(qc))
        # usercart.objects.filter(cproduct_name=pname).delete()
        usercart.objects.filter(cprod_id=pid).delete()
        qc=usercart.objects.filter(cusername=loguser)
        print("after "+str(qc))
    return render(request,"usercart.html")

def removefromuserproducts(request):
    loguser=request.GET['loguser']
    pid=request.GET['pid']
    pname=request.GET['pname']
    print(pname)
    print("before " +str(product.objects.filter(product_uname=loguser)))
    product.objects.filter(id=pid).delete()
    print("after " +str(product.objects.filter(product_uname=loguser)))
    return render(request,"myproducts.html")

def search_in_site(request):
    itemname=request.GET['itemnamesearch']
    pname=product.objects.filter(product_name__icontains=itemname)
    pcat=product.objects.filter(product_category__icontains=itemname)
    pprice=product.objects.filter(product_price__icontains=itemname)
    print(pname)
    productcount=usercart.objects.filter(cusername=request.user).count()
    if pcat.count()>0:
        return render(request,"search_in_site.html",{'pcount':productcount,'allProds':allProds,'founditems':pcat})
    elif pprice.count()>0:
        return render(request,"search_in_site.html",{'pcount':productcount,'allProds':allProds,'founditems':pprice})
    else:
        return render(request,"search_in_site.html",{'pcount':productcount,'allProds':allProds,'founditems':pname})


def open_search(request):
    productcount=usercart.objects.filter(cusername=request.user).count()
    return render(request,"search_in_site.html",{'pcount':productcount})


def products(request,myid):
    products=product.objects.filter(id=myid)
    productcount=usercart.objects.filter(cusername=request.user).count()
    return render(request,"productview.html",{'prod':products[0],'pcount':productcount})

def logtoindex(request):
    return render(request,"index.html")

def addproduct(request):
    if request.method=="POST":
        aproduct_uname=request.user
        aproduct_name=request.POST.get('uprodname')
        aproduct_icon=request.FILES['uprodicon']
        aproduct_price=request.POST.get('uprodprice')
        aproduct_quantity=request.POST.get('uprodquantity')
        aproduct_desc=request.POST.get('uproddesc')
        aproduct_cat=request.POST.get('uprodcat')
        print(type(aproduct_icon))
        l1=str(aproduct_icon)
        l=l1.split('.')
        print(l)
        if l[1].lower()=="png" or l[1].lower()=="jpg" or l[1].lower()=="jpeg":
            print("in here")
            c=product(product_uname=aproduct_uname,product_name=aproduct_name,product_icon=aproduct_icon,product_price=aproduct_price,product_quantity=aproduct_quantity,product_desc=aproduct_desc,product_category=aproduct_cat)
            c.save()
        else:
            print("in err")
            messages.error(request," Please upload image only") 
    productcount=usercart.objects.filter(cusername=request.user).count()
    params={'pcount':productcount}
    return render(request,"addproduct.html",params)
    


def signup(request):
    if request.method=="POST":
        susername=request.POST.get('susername')
        spassword=request.POST.get('spassword')
        sfullname=request.POST.get('sfullname')
        semailid=request.POST.get('semail')
        smobile=request.POST.get('smobile')
        sdob=request.POST.get('sbday')
        scountry=request.POST.get('scountry')
        a=signupUser(username=susername,password=make_password(spassword),sfullname=sfullname,semailid=semailid,smobile=smobile,sdob=sdob,scountry=scountry)
        a.save()
    return render(request,"signup.html")

def loginuser(request):
    if request.method=="POST":
        lusername=request.POST['lusername']
        lpassword=request.POST['lpassword']
        print(lusername,lpassword)
        user=authenticate(username=lusername,password=lpassword)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('index')
    return render(request,"loginuser.html")

def logoutuser(request):
    logout(request)
    return redirect('index')

def check_user(request):
    uname=signupUser.objects.filter(username=request.GET['echeck'])
    if uname:
        return HttpResponse("taken")
    else:
        return HttpResponse("available")

def check_imgfile(request):
    filetype=request.GET['checkfile']
    l=filetype.split('\\')
    l1=l[2].split('.')
    if l1[1].lower()=="png" or l1[1].lower()=="jpg" or l1[1].lower()=="jpeg":
        return HttpResponse("ok")
    else:
        return HttpResponse("nook")

def selected_order(request):
    olist=request.GET['orderlis']
    print(olist)
    productcount=usercart.objects.filter(cusername=request.user).count()
    return render(request,"final_order_page.html",{'ok':olist,'pcount':productcount,'allProds':allProds,})


