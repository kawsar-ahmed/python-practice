import time
from importlib import import_module
from django.http import HttpResponse
from django.conf import settings

class BlockingMiddleWare(object):

    def process_request(self, request):
		#import pdb;pdb.set_trace()
		if request.META.get('REMOTE_ADDR') == "192.168.100.112":
			return HttpResponse("Invalid IP");
