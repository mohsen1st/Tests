from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'jobs/home.html') #render function requires some HTML files, the word 'request' is default