from django.urls import path
from Medi.views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('home/', home, name='home'),
    path('profile/',profile,name="profile"),
    path('doctor/',doctor,name="doctor"),
    path('availability/',availability,name="availability"),
    path('report/', report, name='report'),
    path('locator/', locator, name='locator'),
    path('logout/', logout, name='logout'),
    path('appointment/', appointment_page, name='appointment-page'),
    path('availability/<int:doctor_id>/', doctor_availability, name='doctor_availability')
]
    
