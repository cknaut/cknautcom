from django.shortcuts import render
from django.template import RequestContext
from random import randint
import json
import urllib2

#Advice API
ADVICEURL = 'http://api.adviceslip.com/advice'

def index(request):
    random_color, font_color = get_random_hex_code()
    context = {'random_color' : random_color, 'font_color' : font_color, 'advice' : get_advice}
    return render(request, 'landingpage/base.html', context) 

#Generating random color hex-code and fitting contrast color (b/w)
def get_random_hex_code():
    r = lambda: randint(0,255)
    R = r()
    G = r()
    B = r()
    random_color = '#%02X%02X%02X' % (R,G,B)
    #assiging correct font color (black or white) 
    if (R+G+B)/3.0 < 128:
        return(random_color, "#FFFFFF")
    else:
        return(random_color, "#000000")
        
#Gettin random advice from advice API
def get_advice():
    response = urllib2.urlopen(ADVICEURL)
    advice_json = json.loads(response.read())
    return advice_json["slip"]["advice"]

