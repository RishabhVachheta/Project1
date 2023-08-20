from django.urls import path
from app1.views import *

urlpatterns = [
   path('data/',data),
   path('',index,name="index1"),
   path('product-all/',productall),
   path('product-filter/<int:id>/',productfilter),
   path('login/',login , name="login"),
   path('Logout/',Logout,name = "Logout"),
   path('register/',register),
   path('product-get/<int:id>/',productget,name="productdetails"),
   path('profile',profile,name = "profile"),
   path('buynow/',buynow,name = "buy"),
   path('ordertable/',ordertable,name = "myorder"),
   path('successview/',ordersucess,name = "ordersucessview")
] 