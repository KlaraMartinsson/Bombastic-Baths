from django.shortcuts import render

def home_page(request):
    return render (request, "home/index.html")

def our_story(request):
    return render (request, "home/about.html")

def privacy_policy(request):
    return render (request, "home/privacypolicy.html")
