from datetime import date
import datetime
from telnetlib import STATUS
from unicodedata import name
from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .models import Users, Notes
# Create your views here.


class Home(View):
    def get(self, request):
        users = Users.objects.all()        
        notes  = Notes.objects.filter().order_by("-id")[:20]
        return render(request, "main/index.html", {"users": users, "notes" : notes})
    
class NoteView(View):
    def get(self, request, id=0):
        if id == 0: return HttpResponseRedirect('/')
        note = Notes.objects.filter(id=id)
        return render(request, "main/note.html", {"note": note})

def add_note(request):
    if request.method == 'POST':
       user_id =  request.POST.get("user")
       title = request.POST.get("title")
       text = request.POST.get("text")
       date = datetime.datetime.now()
       note = Notes()
       note.user = Users.objects.get(id=user_id)
       note.title = title
       note.text = text
       note.date = date
       note.save()
       return HttpResponseRedirect('/')
    users = Users.objects.all()
    return render(request, "main/add_note.html", {"users": users})

def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        birthday = datetime.datetime.strptime(request.POST.get('birthday'), '%Y-%m-%d')
        bio = request.POST.get("bio")
        status = request.POST.get('status')
        user = Users()
        user.name = name
        user.birthday = birthday
        user.bio = bio
        user.status = status
        user.save()
        return HttpResponseRedirect('/')
    return render(request, "main/add_user.html")