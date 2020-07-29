from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    request_str = str(type(request))
    requests = dir(request)
    request_str += '。'.join(requests)
    # request_str = request.headers
    # request_str = request.read()
    return HttpResponse(request_str)