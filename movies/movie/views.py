from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm
# Create your views here.

def movie_review(request):
    return render(request,'index.html')

def create_view(request):
    frm=MovieForm()
    if request.POST:
        frm=MovieForm(request.POST)
        if frm.is_valid:
            frm.save()
        else:
            frm=MovieForm()
    return render(request,'create.html',{'frm':frm})

def list_view(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})

def edit_view(request):
    return render(request,'edit.html')