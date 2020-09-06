from django.http import HttpResponse
from random import randint
import json

def vista1(request):
    return HttpResponse("django wow")
def countusergroup(request):
    data = []
    r = lambda: randint(0,255)
    data.append({'value': 'mathi','label': 'usuario', 'color': '#%02X%02X%02X' % (r(),r(),r())})
    return HttpResponse(json.dumps(data), content_type='application/json; utf-8')