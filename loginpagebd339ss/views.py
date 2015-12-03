from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout

def login_url(request):
    if request.method == 'POST':
            #percent-encoding
      
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user.is_active:
                login(request, user)
                return HttpResponse ("Success")
    return render(request, 'landingpage/login.html')   
