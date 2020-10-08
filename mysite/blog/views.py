from django.shortcuts import render
from blog.models import Postagem
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
# Create your views here.

def home(request):
    postagens = Postagem.objects.all().order_by("-data_criacao") #pega todos as postagens do banco e joga na lista 'post'
    return render(request,'home.html',{'postagens':postagens})

def examples(request):
    return render(request,'examples.html',{})

def detalhe_post(request,pk):
    postagem = Postagem.objects.get(pk=pk)
    return render(request,'detalhe_post.html',{'postagem':postagem})

def adicionar_postagem(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            postagem = form.save(commit=False)
            postagem.autor = request.user
            postagem.data_publicacao = timezone.now()
            postagem.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request,'adicionar_postagem.html',{'form':form})

def edit_postagem(request,pk):
    postagem = get_object_or_404(Postagem,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=postagem)
        if form.is_valid():
            postagem = form.save(commit=False)
            postagem.autor = request.user
            postagem.data_publicacao = timezone.now()
            postagem.save()
            return redirect('home')
    else:
        form = PostForm(instance=postagem)

    return render(request,'edit_postagem.html',{'form':form})

