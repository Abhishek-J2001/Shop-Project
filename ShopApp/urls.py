from django.urls import path
from ShopApp import views
urlpatterns = [
    path('indexpage/',views.indexpage, name="indexpage"),
    path('catpage/', views.catpage, name="catpage"),
    path('savedata/', views.savedata, name="savedata"),
    path('catdisplay/', views.catdisplay, name="catdisplay"),
    path('editpage/<int:dataid>/', views.editpage, name="editpage"),
    path('updatedata/<int:dataid>/', views.updatedata, name="updatedata"),
    path('deletecat/<int:dataid>/', views.deletecat, name="deletecat"),

    path('propage/', views.propage, name="propage"),
    path('savedat/', views.savedat, name="savedat"),
    path('prodisplay/', views.prodisplay, name="prodisplay"),
    path('editpag/<int:dataid>/', views.editpag, name="editpag"),
    path('updatedat/<int:dataid>/', views.updatedat, name="updatedat"),
    path('deletepro/<int:dataid>/', views.deletepro, name="deletepro"),

    path('admin_login/',views.admin_login, name="admin_login"),
    path('adminlogin/', views.adminlogin, name="adminlogin"),
    path('admin_logout/',views.admin_logout, name="admin_logout"),
    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('deletecon/<int:dataid>/', views.deletecon, name="deletecon")


]