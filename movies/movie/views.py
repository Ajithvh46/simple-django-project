from django.shortcuts import render

# Create your views here.

def movie_review(request):
    movie_details={
        'movie_data':[{
        'title':'Interstellar',
        'year':2014,
        'summary':'Science fiction',
        'success':True
        },
        {'title':'Inception',
        'year':2010,
        'summary':'Science fiction',
        'success':True
        },
        {
        'title':'Marco',
        'year':2024,
        'summary':'Action movie',
        'success':True
        },
        {
        'title':'Goat',
        'year':2024,
        
        'success':False
        }
        ]
        
    }
    return render(request,'index.html',movie_details)
def create_view(request):
    return render(request,'create.html')

def list_view(request):
    return render(request,'list.html')

def edit_view(request):
    return render(request,'edit.html')