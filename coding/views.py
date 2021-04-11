from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm

# Create your views here.

def home(request):
    return render(request, 'coding/index.html')
    

def viewProblem(request, id):
    problem = Code.objects.get(id=id)
    exampleList = problem.example.split('. ')
    inputList = problem.input_format.split('. ')
    outputList = problem.output_format.split('. ')
    constaintList = problem.constaints.split('. ')
    context = {'problem': problem,
               'exampleList': exampleList, 'inputList': inputList, 'outputList': outputList,
               'constaintList': constaintList
               }
    return render(request, 'coding/view_problem.html', context)

def compile(request, id):
    problem = Code.objects.get(id=id)
    context = {'problem': problem}
    return render(request, 'coding/compiler.html', context)


def viewSourceCode(request, id):
    problem = Code.objects.get(id=id)
    return redirect(problem.problem_sorceCode)


def viewVideoLink(request, id):
    problem = Code.objects.get(id=id)
    return redirect(problem.problem_videoLink)


def viewAllProblems(request):
    problems = Code.objects.all()
    context = {'problems':problems}
    return render(request, 'coding/all_problem.html', context)


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')

		context = {'form': form}
		return render(request, 'coding/register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'coding/login.html', context)


def logoutUser(request):
	logout(request)
	return redirect('login')


def facts(request):
	return render(request, 'coding/programmingFacts.html')


def news(request):
	return render(request, 'coding/programmingNews.html')
