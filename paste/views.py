from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from paste.models import Paste
from django.utils import timezone
# Create your views here.

def index(request):
    latestPasteList = Paste.objects.order_by('-date')
    context = {'latestPasteList' : latestPasteList,}
    return render(request, 'PasteBin/index.html', context)

def SavePaste(request):
    paste = Paste(title = request.POST.get('title'), text = request.POST.get('text'), date =  timezone.now());
    paste.save()
    return index(request)
