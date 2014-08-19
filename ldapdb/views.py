from django.shortcuts import render
from django.http.response import HttpResponse
import datetime

import importlib
from urllib import unquote
import imghdr
from base64 import decodestring

# Create your views here.

def file(request, module, base_dn, model, pk, attr):
    
    _m = importlib.import_module(module)
    modelClass = getattr(_m, model)
    modelClass.base_dn = unquote(base_dn)
    
    instance = modelClass.objects.values(attr).get(pk=pk)
    
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now 
    data = instance[attr]
    
    imageType = imghdr.what('', h=data)
    if imageType:
        content_type = 'image/%s' % imageType
    else:
        content_type = 'application/octet-stream'
    
    response = HttpResponse(data, content_type=content_type)
    if not imageType:
        response['Content-Disposition'] = 'attachment; filename="foo.xls"'
    return response