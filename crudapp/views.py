from django.shortcuts import render, redirect
from .forms import StudentRegistration
from. models import User
# Create your views here.




# Show Data
def addandshow(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'crudapp/addandshow.html',{'form':fm, 'stu':stud})    


# UPDARE DATA
def update(request,id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        fm =StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')

    else:
        pi = User.objects.get(pk=id)
        fm =StudentRegistration(instance=pi)

    return render(request,'crudapp/update.html',{'form':fm})







# dELETE dATA
def delete(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return redirect('/')

    return render(request, 'crudapp/addandshow.html')    
