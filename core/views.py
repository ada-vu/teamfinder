from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'core/signup.html')

def group_form(request):
    return render(request, 'core/group_form.html')