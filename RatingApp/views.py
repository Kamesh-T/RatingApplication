from django.shortcuts import render,redirect
from .models import RatingTable
from .forms import RatingTableForm


# Create your views here.

def RatingTable_View(request):
    form = RatingTableForm()
    if request.method == 'POST':
        form = RatingTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')
    return render(request,'RatingApp/rating.html',{'data':form})

def Success_view(request):
    wish='thank you!!'
    return render(request,'RatingApp/success.html',{'data':wish})

def Result_view(request):
    Rating_details=RatingTable.objects.all()
    return render(request,'RatingApp/result.html',{'data':Rating_details})

def Start_view(request):
    data="Welcome to Rating Application"
    return render(request,'RatingApp/start.html',{'data':data})
    