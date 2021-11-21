from django.http import request
from django.shortcuts import redirect, render
from dbtest.models import MyBoard
from django.utils import timezone


def index(request):
    return render(request, 'index.html', {'list': MyBoard.objects.all()})


def detail(request,id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})


def updateForm(request, id):
    return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})


def updateRes(request):
    id = request.POST['id']
    mytitle =request.POST['mytitle']
    mycontent  = request.POST['mycontent']

    myboard = MyBoard.objects.filter(id=id)
    resultTitle = myboard.update(mytitle=mytitle)
    resultContent = myboard.update(mycontent=mycontent)

    if resultTitle + resultContent == 2:
        return redirect('detail/'+ id)
    else:
        return redirect('updateform/'+id)

def delete(requst, id):
    result_delete = MyBoard.objects.filter(id=id).delete()
    
    if result_delete[0] == 1:
        return redirect('index')
    else:
        return redirect('detail/'+id)


def insertForm(request):
    return render(request, 'insert.html')



def insertRes(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']


    result = MyBoard.objects.create(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now())
    #MyBoard(myname=myname, mytitle=mytitle, mycontent=mycontent, mydate=timezone.now()).save()


    if result:
        return redirect('index')
    else:
        return redirect('insertform')