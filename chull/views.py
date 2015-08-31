from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict

from django.template import RequestContext, loader

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    #import pdb; pdb.set_trace()
    list = ["item 11","item 12","item 13","item 14"]
    template = loader.get_template(r'list.html')
    context = RequestContext(request, {
		'header_text':"List",
        'list': list,
		'ip':get_client_ip(request),
		'Remote_ip':request.META.get('HTTP_HOST')
	})
    return HttpResponse(template.render(context))

def xyz(request):
    dictionary=OrderedDict([("Name","Saimum"),("Age",None),("Phone","12345678912"),("E-mail","saimum@divine-it.net")])
	
    template = loader.get_template(r'dict.html')
    context = RequestContext(request, {
		'header_text':"Dictionary",
		'dictionary':dictionary,
	})
    return HttpResponse(template.render(context))
	
def test(request):
	return HttpResponse("From Chull App")
	
	