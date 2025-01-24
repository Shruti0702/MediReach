from django.urls import path
from Medi.views import *

urlpatterns = [
    path('login',login,name='login'),
    path('signup',signup,name='signup'),
    path('home',home,name='home'),
    path('doc_home',doc_home,name='doc_home'),
    path('report',report,name='report'),
    path('locator',locator,name='locator'),
    path('logout',logout,name='logout')
]