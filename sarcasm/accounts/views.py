from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'home.html',{})	

def register(request):
	return render(request,'register.html',{})

def leaderboard(request):
	return render(request,'leaderboard.html',{})

def instructions(request):
	return render(request,'instructions.html',{})

def forum(request):
	return render(request,'forum.html',{})

def prize(request):
	return render(request,'prize.html',{})				

