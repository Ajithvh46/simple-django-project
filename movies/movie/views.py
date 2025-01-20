from django.shortcuts import render
from . models import MovieInfo
# Create your views here.

def movie_review(request):
    return render(request,'index.html')

def create_view(request):
    if request.POST:
        title=request.POST.get('title')
        year=request.POST.get('year')
        description=request.POST.get('summary')

        movie_obj=MovieInfo(title=title,year=year,description=description)
        movie_obj.save()
    return render(request,'create.html')

def list_view(request):
    movie_set=MovieInfo.objects.all()
    print(movie_set)
    return render(request,'list.html',{'movies':movie_set})

def edit_view(request):
    return render(request,'edit.html')