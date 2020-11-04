from django.shortcuts import render
from .models import Job #to show database models in a webpage
# Create your views here.
def home(request):
    jobs = Job.objects #this will fetch all job objects from the database for us to work with
    return render(request, 'jobs/home.html', {'jobs_list': jobs}) #render function requires some HTML files, the word 'request' is default | 
    # the dictionary at the top of the line above prints the jobs