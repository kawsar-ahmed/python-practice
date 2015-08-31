from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from django.template import RequestContext, loader
from .forms import ContactForm
from django.http import HttpResponseRedirect

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def list(request):
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

def dict(request):
    dictionary=OrderedDict([("Name","Saimum"),("Age",None),("Phone","12345678912"),("E-mail","saimum@divine-it.net")])
    
    template = loader.get_template(r'dict.html')
    context = RequestContext(request, {
        'header_text':"Dictionary",
        'dictionary':dictionary,
    })
    return HttpResponse(template.render(context))

def input_info(request):
    template = loader.get_template(r'get_info.html')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        formData = { 
        'name' : request.POST.get('name',''),
        'age' : request.POST.get('age',''),
        'phone' : request.POST.get('phone',''),
        'email' : request.POST.get('email','') }
        
        import models
        models.connect_db()
        new_user = models.User(request.POST.get('name',''), request.POST.get('age',''), request.POST.get('phone',''), request.POST.get('email',''))
        models.add_record(new_user)
        models.update_db()
        
    # if a GET (or any other method) we'll create a blank form
    else:
        formData = None
    context = RequestContext(request, {
        'header_text':"Provide Information",
        'formData' : formData
        })
    return HttpResponse(template.render(context))

def validate(formdata):
    import formencode
    from formencode import validators

    validator = validators.Int()
    for key, value in formdata.items:
        validator.