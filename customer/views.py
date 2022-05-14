from django.shortcuts import render, HttpResponse

#Create your views here.
def index(request):
    return render(request, 'index.html')

def add(request):
    rp = int(request.GET['rp'])
    op = int(request.GET['op'])
    osp = int(request.GET['onp'])
    sp = int(request.GET['sp'])
    pp = int(request.GET['pp'])
    res = rp + op + osp + sp + pp
    return render(request, "index.html", {"result": res})

