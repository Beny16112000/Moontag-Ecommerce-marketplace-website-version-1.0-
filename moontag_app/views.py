from django.shortcuts import redirect, render
from moontag_app.models import Product
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import moontag_project.settings as settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str 
from . tokens import generate_token


# Create your views here.

def home(request):
    return render(request,'index.html')

def register1(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        # User checks for regisretions
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Try other username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "The Email already exist! try new email")
            return redirect('home')

        if len(username) > 20:
            messages.error(request, "user name must be less than 20 charecters")

        if pass1 != pass2:
            messages.error(request, "Password didn't match!")
        #end


        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your Account successfully created, We have sent you a confirmation email, please confirm your email adress for activate your account")

        # Welcome email
        subject = "Welcome back to the biggest brand Moontag"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Moontag  \n We have sent you a confirmation email, please confirm your email adress for activate your account \n\n Thank you ! \n Moontag Brand "
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Adress confirm
        current_site = get_current_site(request)
        email_subject = "Confirm your email @ moontag - django login!"
        message2 = render_to_string('email_confirmation.html',{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)  
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email]
        )
        email.fail_silently = True
        email.send()

        return redirect('login1')

    return render(request,'register.html')


   
def login1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "index.html", {'fname': fname})

        else:
            messages.error(request, 'Bed credentials')
            return redirect('home')


    return render(request,'login.html')


    
def logout1(request):
    logout(request)
    messages.success(request, "You are logged out")
    return redirect('home')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')

def usersdisplay(request):
    all_users = User.objects.all
    return render(request, 'account.html',{'all':all_users})


def productdisplay(request):
    all_products = Product.objects.all
    return render(request, 'product_display.html',{'all':all_products})

#https://www.youtube.com/watch?v=cRbGNk1-BtA
"""# the game with the model,form,views and with the data base
def add(request):   
    form=ExpenseForm
    if request.method=="POST":
        form=ExpenseForm(request.POST)
        name=form.data["name"]
        date=form.data["date"]
        category=form.data["category"]
        amount=int(form.data["amount"])+random.randrange(1,50)
        e=Expense(name=name,amount=amount,date=date,category=category)
        e.save()
        return display(request, "Added Successfully!"
"""
# לשאול את טל איך אני יוצר עוד רמות למתשמשים כמו שיצרתי
# לשאול את טל איך אני מציג על המסך את התמונה ב - Product display