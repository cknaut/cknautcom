from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout

import os
pw = os.environ.get('BD339SSPW')
def login_url(request):
    if request.method == 'POST':
            password = request.POST['password']
            if password==pw:
                return HttpResponse ("Success")
    return render(request, 'landingpage/login.html')   
