from django.shortcuts import render
from django.template import RequestContext
from random import randint
import json
import urllib2

def index(request):
    context = {'fortune' : get_fortune}
    return render(request, 'landingpage/base.html', context) 
       
#Gettin random fortune from fortune API
def get_fortune():
    response = urllib2.urlopen("http://www.iheartquotes.com/api/v1/random?format=json&max_characters=150&width=60&source=esr+humorix_misc+humorix_stories+joel_on_software+macintosh+math+mav_flame+osp_rules+paul_graham+prog_style+subversion+1811_dictionary_of_the_vulgar_tonguecodehappy+fortune+liberty+literature+misc%20murphy+oneliners+riddles+rkba+shlomif+shlomif_fav+calvin+simpsons_cbg+simpsons_chalkboard+simpsons_homer+simpsons_ralph+south_park")
    fortune_json = json.loads(response.read())
    fortune = fortune_json["quote"].replace("\t", "&nbsp&nbsp&nbsp&nbsp")
    fortune = fortune.replace("\n", "<br />")
    return fortune

