from django.shortcuts import render

# Create your views here.

def movie_review(request):
    return render(request,'index.html')

def create_view(request):
    if request.POST:
        print(request.POST.get('title'))
        print(request.POST.get('year'))
        print(request.POST.get('summary'))
    return render(request,'create.html')

def list_view(request):
    movie_details={
        'movie_data':[{
        'title':'Interstellar',
        'year':2014,
        'summary':'Science fiction',
        'success':True,
        'img':'interstellar.jpg',
        },
        {'title':'Inception',
        'year':2010,
        'summary':'Science fiction',
        'success':True,
        'img':'inception.jpg',
        },
        {
        'title':'Marco',
        'year':2024,
        'summary':'Action movie',
        'success':True,
        'img':'marco1.jpg',
        },
        {
        'title':'Goat',
        'year':2024,
        'summary':'',
        'success':False,
        'img':'goat.jpg',
        }
        ]
        
    }

    return render(request,'list.html',movie_details)

def edit_view(request):
    return render(request,'edit.html')