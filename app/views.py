from django.shortcuts import render

def user_lib(request):
    return render(request, 'user_lib.html')

def user_recs(request):
    return render(request, 'user_recs.html')

def book_search(request):
    return render(request, 'book_search.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')