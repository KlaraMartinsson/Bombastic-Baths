from django.shortcuts import render


def home_page(request):
    return render (request, 'home/index.html')


def our_story(request):
    return render (request, 'home/about.html')


def privacy_policy(request):
    return render (request, 'home/privacypolicy.html')


def faq(request):
    return render (request, 'home/faq.html')

# Custom error views
def custom_403(request, exception=None):
    return render(request, '403.html', status=403)


def custom_404(request, exception=None):
    return render(request, '404.html', status=404)


def custom_405(request, exception=None):
    return render(request, '405.html', status=405)


def custom_500(request, exception=None):
    return render(request, '500.html', status=500)