from django.shortcuts import render, get_object_or_404
from .models import Job #to show database models in a webpage
# Create your views here.
def home(request):
    jobs = Job.objects #this will fetch all job objects from the database for us to work with
    return render(request, 'jobs/home.html', {'jobs_list': jobs}) #render function requires some HTML files, the word 'request' is default | 
    # the dictionary at the top of the line above prints the jobs

def detail(request, job_id): #the job_id comes from the url patter we defined
    job_detail = get_object_or_404(Job, pk=job_id) #pk is the unique id that is created when a record is created, counting from 1
    return render(request, 'jobs/detail.html', {'jobsss':job_detail})