from django.shortcuts import render

# Create your views here.
def vijayy(request):
    d={'name':'VIJAY','age':25,'hobbies':['cricket','chess','volleyball']}
    return render(request,'vijayy.html',context=d)

def vijayy2(request):
    return render(request,'vijayy2.html')