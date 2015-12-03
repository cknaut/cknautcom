from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.http import redirect

import os
pw = os.environ.get('BD339SSPW')
def login_url(request):
    if request.method == 'POST':
            password = request.POST['password']
            if password==pw:
                return redirect ("http://31.24.12.49/")
    return render(request, 'landingpage/login.html')   



