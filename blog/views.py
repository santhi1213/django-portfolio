from django.shortcuts import render, get_object_or_404
from .models import Data

def all_blogs(request):
    blog = Data.objects.order_by('date')
    return render(request,'blog/all_blogs.html', {'data':blog})


def details(request, blog_id):
    blog = get_object_or_404(Data, pk=blog_id)
    return render( request, 'blog/details.html', {'blog':blog})