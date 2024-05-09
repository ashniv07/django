from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, "home.html", {})


def authView(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {'form':form})

def info_form(request):
    if request.method == 'POST':
        info = request.POST.get('info', '')
        info1 = request.POST.get('info1', '')
        info2 = request.POST.get('info2', '')
        return render(request, 'info_display.html', {'info': info, 'info1':info1, 'info2':info2})
    return render(request, 'info_form.html')   
