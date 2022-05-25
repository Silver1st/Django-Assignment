from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from taskapp.models import Incident

# Create your views here.

def list_todo_items(request):
    return render(request,'dashboard2.html')

def home(request):
    return render(request,'dashboard2.html')

def signup(request):
    if request.method == "POST" :
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pwd']
        pass2 = request.POST['cpwd']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()

        messages.success(request, "your account has been successfully created")

        return redirect('signin')

    return render(request, 'register.html')

def signin(request):
    if request.method == "POST" :
        username = request.POST['username']
        pass1 = request.POST["pwd"]

        user = authenticate(username = username, password = pass1 )

        if user is not None :
            login(request, user)
            u_name = user.username
            return render(request, 'dashboard2_updated.html', {'u_name': u_name})

        else :
            messages.error(request, "Please check the username or password again")

    return render(request, 'login.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")

def incident(request):
    if request.method == 'POST':
        location = request.POST['Location']
        incident_department = request.POST.get("Idpt")
        date = request.POST.get("dt")
        incident_location = request.POST.get("Iloc")
        initial_severity = request.POST['isv']
        suspected_cause = request.POST.get("sc")
        immediate_action_taken = request.POST.get("iat")
        sub_incident_type = request.POST.get("checks[]")

        incident = Incident(location=location,incident_department=incident_department,date=date,incident_location=incident_location,initial_severity=initial_severity,suspected_cause=suspected_cause,immediate_action_taken=immediate_action_taken,sub_incident_type=sub_incident_type)
        incident.save()
    return render(request,'incident.html')
