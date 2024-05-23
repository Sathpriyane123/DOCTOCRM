from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from datetime import datetime
from django.utils import timezone
from django.contrib.auth import authenticate,logout
from django.contrib.auth.models import auth

from.models import *

# Create your views here.

def home(request):
    return render(request,'login.html')
def login(request):
    if request.method=='POST':
        email=request.POST["email1"]
        password=request.POST["password"]
        res=logins.objects.filter(email=email,password=password)
        # res=logins.authenticate(username=username, password=password)
        print(res)
        if res.exists():
            res1=logins.objects.get(email=email)
            return render(request, 'dash.html',{'data':res1})
        else:
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def signup_post(request):
    if request.method=='POST':
        username=request.POST["username"]
        email=request.POST['email']
        password=request.POST["password"]
        repassword=request.POST["repassword"]
        if password!=repassword:
            return render(request,'signup.html',{"key":"password not match"})
        x=logins(email=email,password=password)
        x.save()
        users.objects.create(LOGIN=x,username=username,email=email)
        return redirect('/login')
    else:
        return render(request,'login.html')


def login_post(request):
    e={}
    try:
        if request.method == 'POST':
            email = request.POST["email1"]  # Changed "email1" to "email"
            password = request.POST["password"]
            user =newstaff.objects.filter(Email=email, Password=password).exists()  # Changed "Email" to "email"
            if user:
                return render(request,'dash.html')  # Redirect to 'dash' URL name
            else:
                e['keyl']='invlaid email or password'
                return render(request,'login.html',e)
    except Exception as b:
        print(b)
        e={'keyl': 'error'}
        return render(request, 'login.html',e)

    

def tickets(request):
    tc=ticket.objects.all()
    return render(request,"ticket.html",{'show':tc})
def dele(request,id):
    dele=ticket.objects.get(id=id)
    dele.delete()
    return redirect('ticket')
def user(request):
    return render(request,"user.html")
def newticket(request):
    return render(request,"newticket.html")
def register(request):
    if request.method=='POST':
        subject=request.POST['subject']
        contact=request.POST['contact']
        name=request.POST['name']
        email=request.POST['emailaddress']
        department=request.POST['department']
        cc=request.POST['cc']
        tags=request.POST['tags']
        assignticket=request.POST['assigntickets']
        priority=request.POST['priority']
        service=request.POST['service']
        insertpredefined=request.POST['insertpre']
        insertknowledge=request.POST['insertkn']
        textarea=request.POST['textarea']
        attachments=request.POST['attachments']
        myuser=ticket(subject1=subject,contact1=contact,name1=name,email1=email,department1=department,cc1=cc,tags1=tags,assignticket1=assignticket,priority1=priority,service1=service,insertpredefined1=insertpredefined,insertknowledge1=insertknowledge,textarea1=textarea,attachments1=attachments)
        myuser.save()
        return redirect('ticket')
def ticketwithout(request):
    return render(request,"ticketwithout.html")
def followups(request):
    return render(request,'followups.html')
def search(request):
    abc=Doctor2.objects.all()
    return render(request,'search.html',{'data':abc})
def closed(request,id):
    if request.method =='POST':
        producttype= request.POST.get('producttype')
        product= request.POST.get('product')
        quantity= request.POST.get('quantity')
        price= request.POST.get('price')
        discount= request.POST.get('discount')
        offer= request.POST.get('offer')
        installationdateandtime= request.POST.get('installationdateandtime')
        durationfrom= request.POST.get('durationfrom')
        durationto= request.POST.get('durationto')
        installationtype1= request.POST.get('Installationtype')
        paymenttype= request.POST.get('paymenttype')
        balance= request.POST.get('balance')
        description= request.POST.get('description')
        did=Doctor2.objects.get(id=id)
        closed=Closed.objects.create(producttype=producttype,product=product, quantity=quantity, price=price, discount=discount, offer=offer, installationdateandtime=installationdateandtime,durationfrom=durationfrom, durationto=durationto, installationtype=installationtype1,paymenttype=paymenttype, balance=balance, description=description,did=did)
        closed.save()
        obj = Doctor2.objects.get(id=id)
        obj.status1="closed"
        obj.save()
        e= {'key1' :'saved'}
        return render (request, 'edit.html',e)
    else:
        return render(request,'edit.html')


def intrest(request,id):
    if request.method== 'POST':
        type= request.POST.get('type')
        priority=request.POST.get('priority')
        demodate_and_time= request.POST.get('demodate_and_time')
        producttype= request.POST.get('producttype')
        description= request.POST.get('description')
        did=Doctor2.objects.get(id=id)
        intrest=Insert.objects.create(type=type,  priority= priority, demodate_and_time=demodate_and_time, producttype=producttype, description=description,did=did)
        intrest.save()
        obj =Doctor2.objects.get(id=id)
        obj.status1="insert"
        obj.save()
        e= {'key1' :'saved'}
        return render (request, 'edit.html',e)
    else:
        return render(request,'edit.html')
    

def followup(request):
    if request.method=='POST':
        nextfollowup= request.POST.get('nextfollowup')
        description= request.POST.get('description')
        followup=Followup.objects.create( nextfollowup= nextfollowup, description=description )
        followup.save()
        obj = Doctor2.objects.get(id=id)
        obj.status1="closed"
        obj.save()
        e= {'key1' :'saved'}
        return render (request, 'edit.html',e)
    else:
        return render(request,'edit.html')

    
def notintrest(request):
    if request.method=='POST':
        datetime= request.POST.get('datetime')
        description= request.POST.get('description')
        notin=Notintrested.objects.create(datetime=datetime, description=description)
        notin.save()
        e={'key3': 'saved'}
        return render(request,'edit.html',e)
    else:
        return render(request, 'edit.html')


def rnr(request):
    if request.method=='POST':
         nextcalling=request.POST.get('nextcalling')
         rnr=Rnr.objects.create( nextcalling= nextcalling)
         rnr.save()
         return render(request,'edit.html')



def calr(request):
    if request.method=='POST':
        nextcalling=request.POST.get('nextcalling')
        description=request.POST.get('description')
        clr=Calllater.objects.create(nextcalling=nextcalling, description=description)
        clr.save()
        e={'key3': 'saved'}
        return render(request,'edit.html',e)
    else:
        return render(request, 'edit.html')


def newdoctor(request):
    return render(request,'newdctr.html')
def edit(request,id):
    a=Doctor2.objects.get(id=id)
    B=Closed.objects.filter(did=id)
    return render(request,'edit.html',{'data':a,'cl':B})
def newdctr(request):
    if request.method == 'POST':
        title=request.POST['title']
        name=request.POST['name']
        phone=request.POST['phone1']
        clinic=request.POST['clinic1']
        email=request.POST['email']
        specification=request.POST['specification']
        state=request.POST['state']
        city=request.POST['city'] 
        status=request.POST['status']
        myuser=Doctor2(title1=title,name1=name,phone1=phone,clinic1=clinic,email1=email,specification1=specification,state1=state,city1=city,status1=status)
        myuser.save()
        return redirect("search")
def newproduct(request):
    return redirect('/new-product')
def prodect(request):
    if request.method =='POST':
        name1=request.POST['Product']
        price1=request.POST['Price']
        type1=request.POST['Type']
        if not name1 or not price1 or not type1:
            messages.error(request, "All fields must be filled out.")
        else:
            new_product =newprodect(proname=name1, proprice=price1, protype=type1)
            new_product.save()
    dis=newprodect.objects.all()
    return render(request,'newproduct.html',{'show':dis})

def delete(request,id):
    dele=newprodect.objects.get(id=id)
    dele.delete()
    return redirect('/new-product')

def update(request, id):
    instance = get_object_or_404(newprodect, id=id)

    if request.method == 'POST':
        name1 = request.POST['Product']
        price1 = request.POST['Price']
        type1 = request.POST['Type']
        
        if not name1 or not price1 or not type1:
            messages.error(request, "All fields must be filled out.")
        else:
            instance.proname = name1
            instance.proprice = price1
            instance.protype = type1
            instance.save()
            return redirect('/new-prodect')

    return render(request, '/new-prodect', {'instance': instance}) 
def graph1(request):
    return render(request,"ticket.html")
def leads(request):
    ld=newleads.objects.all()
    return render(request,"leads.html",{'we':ld})
def newlead(request):
    return render(request,"newlead.html")
def register1(request):
    if request.method=='POST':
        status=request.POST['status']
        specialisation=request.POST['specialisation']
        assigned=request.POST['assigned']
        tag=request.POST['tags']
        name=request.POST['name']
        position=request.POST['position']
        emailaddress=request.POST['emailaddress']
        website=request.POST['website']
        phone=request.POST['phone']
        company=request.POST['company']
        address=request.POST['address']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        zipcode=request.POST['zipcode']
        language=request.POST['language']
        discription=request.POST['discription']
        priority=request.POST['priority']
        remark=request.POST['remarks']
        myuser=newleads(Status=status,Specialisation=specialisation,Assigned=assigned,Tag=tag,Name=name,Position=position,Emailaddress=emailaddress,Website=website,Phone=phone,Company=company,Address=address,City=city,State=state,Country=country,Zipcode=zipcode,Language=language,Discription=discription,Priority=priority,Remark=remark)
        myuser.save()
    return render(request,'newlead.html')
def dash(request):
    return render(request,"dash.html")


#main-table//

def maindata(request):
    if request.method == 'POST':
        title=request.POST['title']
        name=request.POST['name']
        phone=request.POST['phone']
        clinic=request.POST['clinic']
        email=request.POST['email']
        specification=request.POST['specification']
        state=request.POST['state']
        city=request.POST['city'] 
        status=request.POST['status']
        # interst
        type=request.POST['type']
        Priority=request.POST['priority']
        DateTime=request.POST['demodate_and_time']
        producttype=request.POST['producttype']
        Description=request.POST['description']
        # followup
        nextfollowup=request.POST['nextfollowup']
        description1=request.POST['description']
        # Notintrested
        dttime=request.POST['datetime']
        description2=request.POST['description']
        # rnr
        day=request.POST['nextcalling']
        # Calllater
        day2=request.POST['nextcalling']
        desc=request.POST['description']
        # closed
        prodtype=request.POST['producttype']
        prodect=request.POST['product']
        quantity=request.POST['quantity']
        price=request.POST['price']
        discount=request.POST['discount']
        offer=request.POST['offer']
        installationdateandtime=request.POST['installationdateandtime']
        durationfrom=request.POST['durationfrom']
        durationto=request.POST['durationto']
        Installationtype=request.POST['Installationtype']
        paymenttype=request.POST['paymenttype']
        balance=request.POST['balance']
        description=request.POST['description']


        myuser=Calldata(title=title,name=name,clinic_name=clinic,phone1=phone,email=email,specialisation=specification,state=state,city=city,status1=status,type_int=type,priority_int=Priority,datetime_int=DateTime,producttype_int=producttype,description=Description,datetime_folloup=nextfollowup,description_folloup=description1,datetime_notint=dttime,description_notint=description2,datetime_rnr=day,datetime_clr=day2,description_clr=desc,product_type_cl=prodtype,product_cl=prodect,quantity_cl=quantity,price_cl=price,discount_cl=discount,balance_cl=balance,payment_type_cl=paymenttype,offer_cl=offer,installing_date_cl=installationdateandtime,installation_type_cl=Installationtype,duration_from_cl=durationfrom,duration_to_cl=durationto,description_cl=description)
        myuser.save()
        return redirect("search")

def update2(request):
    return render(request,'edit2.html')    

def update2(request, id):
    xyz= get_object_or_404(Doctor2,id=id)

    if request.method =='POST':
        title=request.POST.get('title')
        name=request.POST.get('name')
        phone=request.POST.get('phone1')
        clinic=request.POST.get('clinic1')
        email=request.POST.get('email')
        specification=request.POST.get('specification')
        state=request.POST.get('state')
        city=request.POST.get('city')

        if not name or not title or not phone or not clinic or not email or not specification or not state or not city:
            messages.error(request, "All fields must be filled out.")
        else:
            xyz.title1=title
            xyz.name1=name
            xyz.phone1=phone
            xyz.clinic1=clinic
            xyz.email1=email
            xyz.specification1=specification
            xyz.state1=state
            xyz.city1=city
            xyz.save()
            return redirect('/search')
    return render(request,'edit2.html',{'xyz':xyz})
    

def deleteone(request,id):
    a=Doctor2.objects.get(id=id)
    a.delete()
    return redirect('/search')
def settings(request):
    return render(request,'settings.html')
def newstaf(request):
    return render(request,'newstaff.html')

def newstaffs(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        facebook=request.POST.get('facebook')
        linkedin=request.POST.get('linkedin')
        skype=request.POST.get('skype')
        defaultlanguage=request.POST.get('language')
        emailsig=request.POST.get('emailsignature')
        direction=request.POST.get('direction')
        state=request.POST.get('states')
        password=request.POST.get('password')
        abc=newstaff.objects.create(Firstname=firstname,Lastname=lastname,Email=email,Phoneno=phonenumber,Defaultlanguage=defaultlanguage,Emailsig=emailsig,Direction=direction,Facebook=facebook,Linkedin=linkedin,Skype=skype,Defaultstate=state,Password=password)
        abc.save()
        return redirect('/settings')
    else:
        return render(request,'newstaff.html')
    


def custom_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return render(request, "login.html")
    
        



    

