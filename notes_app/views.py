from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Note



#### show all notes
def all_notes(request):
    # return HttpResponse("<h1> Welcome In Django Whith Mohammed Chougrani </h1>")
    all_notes = Note.objects.all()
    context = {
        'all_notes' : all_notes
    }
    return render(request, 'all_notes.html', context)

##### show one notes
def detail(request, slug):
    note = Note.objects.get(slug=slug)
    context = {
        'note' : note
    }
    return render(request, 'note_detail.html', context)