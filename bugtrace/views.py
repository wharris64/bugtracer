from django.shortcuts import render, redirect
from django import forms
from bugtrace.forms import LoginUser
from bugtrace.models import Ticket
from bugtrace.forms import Add_Ticket, Edit, UserAdd
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# from bugtrace.forms import

def index(request):
    html = "index.html"
    ticket = Ticket.objects.all()
    inprog = Ticket.objects.filter(ticket_status='ip')
    invalid =Ticket.objects.filter(ticket_status='iv')
    new = Ticket.objects.filter(ticket_status='n')
    finished = Ticket.objects.filter(ticket_status='f')
    # breakpoint()
    return render(request, html, {'inprog':inprog, 'invalid':invalid, 'new':new, "finished":finished})


@login_required
def authorlist(request):
    html = "authorlist.html"
    authors = User.objects.all()
    return render(request, html, {"authors":authors})

@login_required
def authorview(request, id):
    html = "authorview.html"
    name = User.objects.filter(id=id)
    tickets = Ticket.objects.all()
    working = tickets.filter(ticket_assignee=id)
    filed = tickets.filter(author=id)
    done = tickets.filter(ticket_finisher=id)
    return render(request, html, {"name" : name, "working" : working, "filed":filed, "done":done})

@login_required
def detail(request, id):
    html = "detail.html"
    detail = Ticket.objects.filter(id=id)
    return render(request, html, {"data" : detail})
 


@login_required
def ticketadd(request):
    form = None
    html = "ticket_add.html"

    if request.method == "POST":
        form = Add_Ticket(request.POST)
        
        if form.is_valid():
            data= form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                author=request.user,
                description=data['description'],
            )
            return render(request, 'thanks.html')
    else:
        form = Add_Ticket()
    return render(request, html, {"form": form})



@login_required
def register(request):
    form = None
    html = "useradd.html"

    if request.method == "POST":
        form = UserAdd(request.POST)
        
        if form.is_valid():
            data= form.cleaned_data
            User.objects.create(
                username= data['username'],
                password= data['password']
            )
        return render(request, 'thanks.html')
    else:
        form = UserAdd()
    return render(request, html, {"form": form})

@login_required
def editticket(request, id):
    form = None
    html = 'editticket.html'
    instance = Ticket.objects.get(pk=id)
    if request.method == "POST":
        form = Edit(request.POST, instance=instance)
        
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = Edit(instance=instance)
        return render(request, html, {'form':form})




def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    html = "user_login.html"
    form = LoginUser()
    if request.method == "POST":
        form = LoginUser(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])
            if user:
                login(request, user)
            return redirect(request.GET.get("next", '/'))
    return render(request, html, {"form": form})

@login_required
def inprogress(request, id):
    ticket = Ticket.objects.get(pk=id)
    ticket.ticket_status = "ip"
    ticket.ticket_assignee = request.user
    ticket.ticket_finisher = None
    ticket.save()
    return redirect('/')

@login_required
def invalid(request, id):
    ticket = Ticket.objects.get(pk=id)
    ticket.ticket_status = "iv"
    ticket.ticket_assignee = None
    ticket.ticket_finisher = None
    ticket.save()
    return redirect('/')

@login_required
def finished(request, id):
    ticket = Ticket.objects.get(pk=id)
    ticket.ticket_status = "f"
    ticket.ticket_finisher = ticket.ticket_assignee
    ticket.ticket_assignee = None
    ticket.save()
    return redirect('/')