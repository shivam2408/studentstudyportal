from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import DetailView
from .forms import *

def home(request):
    return render(request, 'dashboard/home.html')

def notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            notes = Notes(Username=request.user, Title = request.POST['Title'], description = request.POST['description'])
            notes.save()
        messages.success(request,f"Notes added from {request.user.username} successfully.")
    else:
        form = NotesForm()
    notes = Notes.objects.filter(Username=request.user)
    context = {'notes': notes, 'form': form}
    return render(request, 'dashboard/notes.html', context)

def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")

class NotesDetailView(DetailView):
    model = Notes

def homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == "on":
                    finished = True
                else:
                    homework_done = False
            except:
                finished = False

            homeworks = Homework(
                user = request.user,
                subject = request.POST['subject'],
                title= request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished,
            )
            homeworks.save()
            messages.success(request,f'Homework Added from {request.user.username}')
    else:
        form = HomeworkForm()

    homework = Homework.objects.filter(user=request.user)

    if len(homework)==0:
        homework_done = True
    else:
        homework_done = False
    context = {'homeworks': homework,
               'homeworks_done':homework_done,
               'form':form,
               }
    return render(request,'dashboard/homework.html',context)

def update_homework(request,pk=None):
    homework = Homework.objects.get(id=pk)
    if homework.is_finished == True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')


def delete_homework(request,pk=None):
    Homework.objects.get(id=pk).delete()
    return redirect("homework")
