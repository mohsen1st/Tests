from django.contrib import admin

from .models import Pet #imports the data from the "models: file in the same folder

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin): #the class inherits from admin.ModelAdmin
    list_display = ['name','species', 'breed', 'age', 'sex'] #to display object names from the admin panel
