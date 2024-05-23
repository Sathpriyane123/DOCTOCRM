from django.contrib import admin
from.models import *
# Register your models here.


class Doctor2Admin(admin.ModelAdmin):
    list_display=('title1','name1','phone1','clinic1','email1','specification1','state1','city1','status1')
admin.site.register(Doctor2,Doctor2Admin)
class newprodectAdmin(admin.ModelAdmin):
    list_display=('proname','proprice','protype')
admin.site.register(newprodect,newprodectAdmin)
class ticketAdmin(admin.ModelAdmin):
    list_display=('subject1','contact1','name1','email1','department1','cc1','tags1','assignticket1','priority1','service1','insertpredefined1','insertknowledge1','textarea1','attachments1')
admin.site.register(ticket,ticketAdmin)
class ClosedAdmin(admin.ModelAdmin):
    list_display=('producttype','product','quantity','price','discount','offer','installationdateandtime','durationfrom','durationto','installationtype','paymenttype','balance','description','cdt','did')
admin.site.register(Closed,ClosedAdmin)
class InsertAdmin(admin.ModelAdmin):
    list_display=('type','priority','demodate_and_time','producttype','description')
admin.site.register(Insert,InsertAdmin)
class FollowupAdmin(admin.ModelAdmin):
    list_display=('nextfollowup','description')
admin.site.register(Followup,FollowupAdmin)
class NotintrestedAdmin(admin.ModelAdmin):
    list_display=('datetime','description')
admin.site.register(Notintrested,NotintrestedAdmin)

class RnrAdmin(admin.ModelAdmin):
    list_display=['nextcalling']
admin.site.register(Rnr,RnrAdmin)

class CalllaterAdmin(admin.ModelAdmin):
    list_display=('nextcalling','description')
admin.site.register(Calllater,CalllaterAdmin)

class newstaffAdmin(admin.ModelAdmin):
    list_display=('Firstname','Lastname','Email','Phoneno','Defaultlanguage','Emailsig','Direction','Facebook','Linkedin','Skype','Defaultstate','Password')
admin.site.register(newstaff,newstaffAdmin)    



