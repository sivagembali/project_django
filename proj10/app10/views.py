from django.shortcuts import render
from firebase import firebase as fab
fa = fab.FirebaseApplication('https://reflected-wind-216512.firebaseio.com/',None)
def showIndex(request):
    return render(request,'index.html')


def registerPage(request):
    d1 =fa.get('Employee/',None)
    if d1 == None:
        key = 101
    else:
        for x in d1:
            key = x
        key = int(key) + 1
    return render(request,'register.html',{'key':key})


def viewsAll(request):
    d1 = fa.get('Employee/',None)
    if d1==None:
        return render(request,'views.html',{'msg':'No Data Available'})
    else:
        return render(request,'views.html',{'d1':d1})


def saveDetails(request):
    id = request.POST.get('idno')
    name = request.POST.get('uname')
    cno = request.POST.get('cno')
    fa.put('Employee/',id,{'name':name,'cno':cno})
    return render(request,'index.html')


def deleteRecord(request):
    idno = request.POST.get('delete')
    fa.delete('Employee/',idno)
    return viewsAll(request)


def updateRecord(request,rid):
    d = fa.get('Employee/'+rid,None)
    return render(request,'register.html',{'key':rid,'name':d['name'],'cno':d['cno']})