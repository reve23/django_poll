from django.shortcuts import render,redirect
from .forms import RegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/polls")
    else:
        form = RegistrationForm()
    return render(request,'register/register.html',{'form':form})