from django.urls import path
from.import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.home),
    path('ticket',views.tickets,name='ticket'),
    path('user',views.user,name='user'),
    path('newticket',views.newticket,name='newticket'),
    path('tickets',views.register,name='tickets'),
    path('deleteone/<int:id>',views.dele,name='deleteone'),
    path('ticketwithout',views.ticketwithout,name='ticketwithout'),
    path('followups',views.followups,name='followups'),
    path('search',views.search,name='search'),
    path('closed/<int:id>',views.closed,name='closed'),
    path('intrest/<int:id>',views.intrest,name='intrest'),
    path('followup/<int:id>',views.followup,name='followup'),
    path('notintrested', views.notintrest,name='notintrested'),
    path('rnr',views.rnr, name='rnr'),
    path('calllater', views.calr, name='calllater'),
    path('newdoctor',views.newdoctor,name='newdoctor'),
    path('newdctr',views.newdctr,name='newdctr'),
    path('newproduct',views.newproduct,name="newproduct"),
    path('new-product',views.prodect,name='new-product'),
    path('deletetwo/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('graph',views.graph1),
    path('leads',views.leads,name='leads'),
    path('',views.newlead),
    path('newlead',views.register1,name='newlead'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update_one/<int:id>',views.update2,name='update1'),
    path('delete/<int:id>',views.deleteone,name='delete1'),
    path('dash',views.dash,name='dash'),
    path('',views.maindata),
    path('login',views.login,name='login'),
    path('login_post',views.login_post,name='login_post'),
    path('signup',views.signup_post,name='signup'),
    path('settings',views.settings,name='settings'),
    path('newstaf',views.newstaf,name='newstaf'),
    path('newstaff',views.newstaffs,name='newstaff'),

    path('logout', views.custom_logout, name='logout'),

    

]