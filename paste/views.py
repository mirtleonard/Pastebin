from django.shortcuts import render
from paste.models import Paste

# Create your views here.

def index(request):
    latestPasteList = Paste.objects.order_by('-date')
    context = {'latestPasteList' : latestPasteList,}
    return render(request, 'PasteBin/index.html', context)
