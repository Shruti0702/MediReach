from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from Medi.models import User
from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from Medi.models import Profile
from Medi.models import Availability 
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def login(req):
    if req.session.get('user_id'):
        return redirect('home')

    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if check_password(password, user.pswd):
                req.session['user_id'] = user.id
                # req.session.set_expiry(3600)  # Session expires in 1 hour
                if(user.doc==0):
                    return redirect('home')
                else:
                    return redirect('doctor')
            else:
                messages.error(req, 'Incorrect password. Please try again.')
        except User.DoesNotExist:
            messages.error(req, 'This email is not registered with us.')

        return redirect('login')

    return render(req, 'login.html')


def signup(req):
    if req.session.get('user_id'):
        return redirect('home')

    if req.method == 'POST':
        email = req.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(req, 'This email is already registered with us.')
            return redirect('signup')


        name = req.POST.get('name')
        password = make_password(req.POST.get('password'))
        city = req.POST.get('city')
        state = req.POST.get('state')
        country = req.POST.get('country')
        user_type = req.POST.get('user_type')
        if user_type == 'doctor':
            doc=1
        elif user_type == 'patient':
            doc=0
        user = User.objects.create(name=name, email=email, doc=doc, pswd=password, city=city, state=state, country=country)
        req.session['user_id'] = user.id
        if(user.doc==0):
            return redirect('home')
        else:
            return redirect('doctor')

    return render(req, 'signup.html')


def home(req):
    user_id = req.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            return render(req, 'home.html', {'email': user.email, 'name': user.name})
        except User.DoesNotExist:
            del req.session['user_id']
            return redirect('login')
    else:
        return redirect('login')


def doctor(req):
    user_id = req.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            return render(req, 'doctor.html', {'email': user.email, 'name': user.name})
        except User.DoesNotExist:
            del req.session['user_id']
            return redirect('login')
    else:
        return redirect('login')


def logout(req):
    if req.session.get('user_id'):
        del req.session['user_id']
    return redirect('login')

def report(req):
    if req.session.get('user_id'):
        return render(req,'report.html')
    return redirect('login')

def locator(req):
    if req.session.get('user_id'):
        return render(req,'locator.html')
    return redirect('login')
def profile(request):
    if request.method=="POST":
        n=request.POST.get('name')
        s=request.POST.get('specialization')
        e=request.POST.get('experience')
        num=request.POST.get('phone')
        mail=request.POST.get('email')
        add=request.POST.get('address')
        
        profile1=Profile(name=n,specialization=s,experience=e,phone=num,email=mail,address=add,date=datetime.today())
        profile1.save()
    return render(request,'profile.html')
    #return HttpResponse("this is profile")
'''def doctor(request):
    return render(request,'doctor.html')'''
'''
def availability(request):
    if request.method == 'POST':
        # Get the form data
        availability_date = request.POST['availability_date']  # Make sure this matches the form field name
        morning_start = request.POST['morning_start']
        morning_end = request.POST['morning_end']
        evening_start = request.POST['evening_start']
        evening_end = request.POST['evening_end']

        # Save the availability to the database
        availability = Availability(
            date=availability_date,
            morning_start=morning_start,
            morning_end=morning_end,
            evening_start=evening_start,
            evening_end=evening_end,
        )
        availability.save()
        messages.success(request, "Availability successfully saved!")
        return redirect('availability')  # Redirect to the availability page or another page after saving

    return render(request, 'availability.html')'''
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Availability

def availability(request):
    if request.method == 'POST':
        if request.user.is_authenticated:  # Ensure user is logged in
            doctor = request.user  # Assign logged-in user as the doctor
        else:
            messages.error(request, "You must be logged in to set availability.")
            return redirect('login')  # Redirect to your login page

        # Get form data
        availability_date = request.POST.get('availability_date')
        morning_start = request.POST.get('morning_start')
        morning_end = request.POST.get('morning_end')
        evening_start = request.POST.get('evening_start')
        evening_end = request.POST.get('evening_end')

        # Ensure the user is a doctor
        if not doctor.doc:  
            messages.error(request, "Only doctors can set availability.")
            return redirect('availability')

        # Save or update availability
        availability, created = Availability.objects.get_or_create(
            doctor=doctor,
            date=availability_date,
            defaults={
                'morning_start': morning_start,
                'morning_end': morning_end,
                'evening_start': evening_start,
                'evening_end': evening_end,
            }
        )

        if not created:  # If already exists, update fields
            availability.morning_start = morning_start
            availability.morning_end = morning_end
            availability.evening_start = evening_start
            availability.evening_end = evening_end
            availability.save()

        messages.success(request, "Availability successfully saved!")
        return redirect('availability')

    return render(request, 'availability.html')

def appointment_page(request):
    """Shows the list of doctors available for booking."""
    doctors = User.objects.filter(doc=True)  # Fetch only doctors

    return render(request, 'appointment.html', {'doctors': doctors})
def doctor_availability(request, doctor_id):
    """Displays available slots for a specific doctor."""
    doctor = get_object_or_404(User, id=doctor_id, doc=True)  # Ensure only doctors are fetched
    availability = Availability.objects.filter(doctor=doctor)

    return render(request, 'doctor_availability.html', {'doctor': doctor, 'availability': availability})
