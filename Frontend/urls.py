from django.urls import path
from Frontend import views

urlpatterns = [
        path('', views.homepage, name= "homepage"),
        path('propage/', views.propage, name= "propage"),
        path('singlepage/<int:proid>/', views.singlepage, name= "singlepage"),
        path('procatpage/<cat_name>/', views.procatpage, name= "procatpage"),
        path('serpage/', views.serpage, name= "serpage"),
        path('aboutpage/', views.aboutpage, name= "aboutpage"),
        path('conpage/', views.conpage, name="conpage"),
        path('savecon/', views.savecon, name="savecon"),
        path('regpage/', views.regpage, name= "regpage"),
        path('savereg/', views.savereg, name="savereg"),
        path('login_page/', views.login_page, name= "login_page"),
        path('user_login/', views.user_login, name= "user_login"),
        path('user_logout/', views.user_logout, name="user_logout"),
]