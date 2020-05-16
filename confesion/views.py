from django.shortcuts import render, redirect
from confesion.models import Confesion, Comentario
from confesion.forms import CommentForm, ConfesionForm

# Create your views here.

def home(request):
    confesiones = Confesion.objects.all()
    comentarios = Comentario.objects.all()
    return render(request, 'home.html', {
        'confesiones' : confesiones,
        'comentarios' : comentarios
    })

def confesion(request, id):
    confesion = Confesion.objects.get(id=id)
    comentario = Comentario.objects.all()
    return render(request, 'confesion.html', {
        'confesion' : confesion,
        'comentario' : comentario
    })

def agregar_comentario(request, id):
    confesion = Confesion.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.confesion = confesion
            comment.save()
            return redirect('confesion', id=confesion.id)
    else:
        form = CommentForm()
    return render(request, 'agregar_comentario.html', {
        'form': form,
        'confesion' : confesion
        })

def agregar_confesion(request):
    if request.method == "POST":
        form = ConfesionForm(request.POST)
        if form.is_valid():
            confesion = form.save(commit=False)
            confesion.confesion = confesion
            confesion.save()
            return redirect('home')
    else:
        form = ConfesionForm()
    return render(request, 'agregar_confesion.html', {'form': form})

