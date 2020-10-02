from django.shortcuts import render
from blog.models import Postagem
# Create your views here.

def home(request):
    postagens = Postagem.objects.all() #pega todos as postagens do banco e joga na lista 'post'
    return render(request,'home.html',{'postagens':postagens})

def examples(request):
    return render(request,'examples.html',{})
