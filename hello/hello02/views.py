from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request, 'hello.html', {'name': 'hong-gd'})




def variables01(request):
    lst = ['java', 'database', 'spring', 'python']
    return render(request, 'variables01.html', {'lst': lst})



def variables02(request):
    dct = {'class': 'ai sw developer', 'name': 'hong-gd'}
    return render(request, 'variables02.html', {'dct': dct})



def forloop(request):
    return render(request, 'for.html', {'number': range(1, 10)})


def if01(request):
    return render(request, 'if01.html', {'user': {'id':'hong-gd', 'pw': '1234'}})

def if02(request):
    return render(request, 'if02.html', {'role': 'manage'})

def href(request):
    return render(request, 'href.html')