from django.db import models

# Create your models here.
#newdoctor




class Doctor2(models.Model):
    title1=models.CharField(max_length=100)
    name1 = models.CharField(max_length=255)
    phone1 = models.CharField(max_length=15)
    clinic1 = models.CharField(max_length=255)
    email1 = models.EmailField()
    specification1=models.CharField(max_length=50)
    state1 = models.CharField(max_length=50)
    city1 = models.CharField(max_length=50)
    status1=models.CharField(max_length=100)



# new product
class newprodect(models.Model):
    
    proname=models.CharField(max_length=50)
    proprice=models.IntegerField()
    protype=models.CharField(max_length=50)

#search and call

#tickets
    
class ticket(models.Model):
    subject1=models.CharField(max_length=100)
    contact1=models.CharField(max_length=100)
    name1=models.CharField(max_length=100)
    email1=models.CharField(max_length=100)
    department1=models.CharField(max_length=100)
    cc1=models.CharField(max_length=100)
    tags1=models.CharField(max_length=100)
    assignticket1=models.CharField(max_length=100)
    priority1=models.CharField(max_length=100)
    service1=models.CharField(max_length=100)
    insertpredefined1=models.CharField(max_length=100)
    insertknowledge1=models.CharField(max_length=100)
    textarea1=models.CharField(max_length=100)
    attachments1=models.FileField()

# closed for search and calls
    
class Closed(models.Model):
    product_type_choice=[
        ('select itiem', 'select item'),
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('both', 'BOTH'),
        ('digital markecting + website', 'Digital Marketing + Website'),
    ]
    product_choice=[
        ('select product', 'Select product'),
        ('doctosmart corporate eye version', 'Doctosmart Corporate Eye version'),
        ('doctosmart basic plan', 'Doctosmart Basic Plan'),
        ('doctosmart corporate version', 'Doctosmart Corporate version'),
        ('doctosmart smart package', 'Doctosmart Smart Package'),
        ('software basic', 'Software Basic'),
    ]
    offer_choice=[
        ('select offer', 'Select offer'),
        ('2 month free tab','2 Month Free tab'),
        ('free tab','Free tab'),
    ]
    paymenttype_choice=[
        ('select payament','Select Payment'),
        ('cash', 'Cash'),
        ('cheque', 'Cheque'),
        ('cod', 'COD'),
        ('upi', 'UPI'),
    ]
    instalation_choice=[
        ('online', 'Online'),
        ('on site','On Site'),
    ]
    producttype= models.CharField(max_length=100, choices=product_type_choice)
    product= models.CharField(max_length=200, choices=product_choice)
    quantity=models.IntegerField()
    price=models.IntegerField()
    discount=models.IntegerField()
    offer=models.CharField(max_length=100, choices=offer_choice)
    installationdateandtime=models.DateTimeField()
    durationfrom=models.DateTimeField()
    durationto=models.DateTimeField()
    installationtype=models.CharField(max_length=60, choices=instalation_choice)
    paymenttype=models.CharField(max_length=100, choices=paymenttype_choice)
    balance=models.IntegerField()
    description=models.TextField(max_length=1000)
    cdt=models.DateTimeField(auto_now_add=True)
    did=models.ForeignKey(Doctor2, on_delete=models.CASCADE)

# intrest search and calls
    
class Insert(models.Model):
    type_choices=[
        ('leads', 'Leads'),
        ('follow up', 'Follow up'),
        ('closable', 'Closable'),
    ]
    priority_choices=[
        ('hot', 'Hot'),
        ('average', 'Average'),
        ('low', 'Low'),
    ]
    producttype_choice=[
        ('select work','Select work'),
        ('online','Online'),
        ('offline', 'Offline'),
        ('both', 'BOTH'),
        ('digital marketing + website','Digital Markecting + website'),
    ]
    type=models.CharField(max_length=100, choices=type_choices)
    priority=models.CharField(max_length=100, choices=priority_choices)
    demodate_and_time=models.DateTimeField()
    producttype=models.CharField(max_length=100, choices=producttype_choice)
    description=models.TextField(max_length=10000)
    did=models.ForeignKey(Doctor2, on_delete=models.CASCADE)

# # search and calls followup
    
class Followup(models.Model):
    nextfollowup=models.DateTimeField(max_length=10)
    description=models.TextField(max_length=10000)

class Notintrested(models.Model):
    datetime=models.DateTimeField(max_length=10)
    description=models.TextField(max_length=1000)

class Rnr(models.Model):
    nextcalling=models.DateTimeField(max_length=10)

class Calllater(models.Model):
    nextcalling= models.DateTimeField(max_length=10)
    description= models.TextField(max_length=1000)



class Calldata(models.Model):
    title=models.CharField(max_length=100)
    name=models.CharField(max_length=200)
    clinic_name=models.CharField(max_length=200)
    phone1=models.CharField(max_length=100, null= True, blank=True)
    phone2=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField()
    specialisation=models.CharField(max_length=100)
    state=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    status1=models.CharField(max_length=100)


    # intrest 
    type_int=models.CharField(max_length=100)
    priority_int=models.CharField(max_length=100)
    datetime_int=models.DateField()
    producttype_int=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    # closed
    product_type_cl=models.CharField(max_length=200) 
    product_cl=models.CharField(max_length=200)
    quantity_cl=models.IntegerField()
    price_cl= models.IntegerField()
    discount_cl=models.IntegerField()
    balance_cl=models.IntegerField()
    payment_type_cl=models.CharField(max_length=100)
    offer_cl=models.CharField(max_length=200)
    installing_date_cl=models.DateField()
    installation_type_cl=models.CharField(max_length=100)
    duration_from_cl=models.DateField()
    duration_to_cl=models.DateField()
    description_cl=models.TextField(max_length=1000)

    # folloup
    datetime_folloup=models.DateTimeField()
    description_folloup= models.TextField(max_length=1000)

    # NOT INTREST
    datetime_notint=models.DateTimeField()
    description_notint=models.TextField(max_length=1000)

    # Rnr
    datetime_rnr= models.DateTimeField()

    # call later
    datetime_clr=models.DateTimeField()
    description_clr=models.TextField(max_length=1000)

# //leads table//
class Leads(models.Model):
    # intrest
    type_int=models.CharField(max_length=100)
    priority_int=models.CharField(max_length=100)
    datetime_int=models.DateField()
    producttype_int=models.CharField(max_length=100)

#// new leads//
    
class newleads(models.Model):
    Status=models.CharField(max_length=50)
    Specialisation=models.CharField(max_length=50)
    Assigned=models.CharField(max_length=50)
    Tag=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    Position=models.CharField(max_length=50)
    Emailaddress=models.CharField(max_length=50)
    Website=models.CharField(max_length=50)
    Phone=models.CharField(max_length=50)
    Company=models.CharField(max_length=50)
    Address=models.CharField(max_length=50)
    City=models.CharField(max_length=50)
    State=models.CharField(max_length=50)
    Country=models.CharField(max_length=50)
    Zipcode=models.CharField(max_length=50)
    Language=models.CharField(max_length=50)
    Discription=models.CharField(max_length=50)
    Priority=models.CharField(max_length=50)
    Remark=models.CharField(max_length=50)


   

# // Reminder tables//
class Reminder(models.Model):
    # follouw up
    datetime_folloup=models.DateTimeField()
    description_folloup= models.TextField(max_length=1000)

    # Rnr
    datetime_rnr= models.DateTimeField()
    description_rnr= models.TextField(max_length=1000)

    # call later
    datetime_clr=models.DateTimeField()
    description_clr=models.TextField(max_length=1000)

    #login and logout
class logins(models.Model):
     email=models.CharField(max_length=50)
     password=models.CharField(max_length=20)

class users(models.Model):
     LOGIN=models.ForeignKey(logins, on_delete=models.CASCADE)
     username=models.CharField(max_length=20)
     email=models.CharField(max_length=50)

# settings

class newstaff(models.Model):
    Firstname=models.CharField(max_length=50,null=True)
    Lastname=models.CharField(max_length=50,null=True)
    Email=models.EmailField(max_length=50,null=True)
    Phoneno=models.IntegerField()
    Defaultlanguage=models.CharField(max_length=50,null=True)
    Emailsig=models.CharField(max_length=50,null=True)
    Direction=models.CharField(max_length=50,null=True)
    Facebook=models.CharField(max_length=50,null=True)
    Linkedin=models.CharField(max_length=50,null=True)
    Skype=models.CharField(max_length=50,null=True)
    Defaultstate=models.CharField(max_length=50,null=True)
    Password=models.CharField(max_length=50,null=True)
    

    

    


    

