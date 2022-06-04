from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from eagro import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.index,name="home"),
    path('mycart',views.mycart,name="mycart"),
    path('usercarts',views.usercarts,name="usercarts"),
    path('removefromcart',views.removefromcart,name="removefromcart"),
    path('removefromuserproducts',views.removefromuserproducts,name="removefromuserproducts"),
    path('search_in_site',views.search_in_site,name="search_in_site"),
    path('open_search',views.open_search,name="open_search"),
    path('addproduct',views.addproduct,name="addproduct"),
    path('myproducts',views.myproducts,name="myproducts"),
    path('products/<int:myid>',views.products,name="products"),
    path('index',views.logtoindex,name="logtoindex"),
    path('signup',views.signup,name="signup"),
    path('loginuser',views.loginuser,name="loginuser"),
    path('logoutuser',views.logoutuser,name="logoutuser"),
    path('check_user',views.check_user,name="check_user"),
    path('check_imgfile',views.check_imgfile,name="check_imgfile"),
    path('selected_order',views.selected_order,name="selected_order"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)