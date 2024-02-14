from django.shortcuts import render,HttpResponseRedirect
from .models import User
from .form import Userform

# Create your views here.
def add(request):
    st =  User.objects.all()
    if request.method == 'POST':
        stu = Userform(request.POST)
        if stu.is_valid():
            stu.save()
            stu = Userform()
    else:
        stu = Userform()
    return render(request,'add.html',{'for':stu , 'st':st})

# create del function
def delete(request,id):
    if request.method == 'POST':
        de = User.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/')

# create update function
def update(request,id):
    if request.method == 'POST':
        up = User.objects.get(pk=id)
        upd =  Userform(request.POST,instance=up) 
        if upd.is_valid():
            upd.save()
            upd = Userform()
    else:
        up = User.objects.get(pk=id)
        upd = Userform(instance=up)
    return render(request,'update.html',{'for':upd})
