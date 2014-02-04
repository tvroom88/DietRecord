from django.http import HttpResponse
from django.shortcuts import render_to_response, RequestContext
from Main.models import *

from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def main(request):
    #polls = Poll.objects.order_by()
    return render_to_response("main.html", RequestContext(request))

@csrf_exempt
def test(request):
    #Parameter
    test = request.POST['test']


    return HttpResponse(test)

@csrf_exempt
def diet_save(request):
    #Parameter
    date = request.POST['date']
    pushUp = int(request.POST['pustUp'])
    sitUp = int(request.POST['sitUp'])

    dietProgram = DietProgram(sitUpCount=sitUp, pushUpCount=pushUp)
    dietProgram.save()

    return HttpResponse(date + str(pushUp) + str(sitUp))