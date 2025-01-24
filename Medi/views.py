from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password, make_password
from Medi.models import User


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
                    return redirect('doc_home')
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
            return redirect('doc_home')

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


def doc_home(req):
    user_id = req.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
            return render(req, 'doc_home.html', {'email': user.email, 'name': user.name})
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
