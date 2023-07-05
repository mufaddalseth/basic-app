from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse


def members(request):
    return HttpResponse("Hello world!")
    # Example 1 - For templating (Jinja will be in key value pair only)
    # name = "YAHOO"
    # return render(request, "home.html", {'name': name})

    # Example 2 -  Query String to take input from user.
    # For multi request processing threading concept use
    # For every request Django creates a object that's why we mentioned request in function.
    # print(request)    # o/p -> <WSGIRequest: GET '/home/'>
    # print(request.META.get("REMOTE_ADDR"))
    # searchterm = request.GET.get("q") 
    # print(searchterm)

    # return HttpResponse("Your Number is {}".format(id))

# # Example of how to connect with database 
from django.db import connection
def run_query(request):
    # Execute your SQL query
    with connection.cursor() as cursor:                 #Context processing if with not used then we have to close the cursor as well
        cursor.execute("SELECT * FROM student")
        results = cursor.fetchall()

    # Pass the results to the template
    for i in results:
        print(i)
    print("Database data received")
    context = {'results': results}
    return render(request, 'home.html', context)

def home(request):
    return render(request, 'home.html')
from courses_section.forms import Courses_Form
def courses(request):
    if request.method == 'POST':
        print("Hello")
        form = Courses_Form(request.POST , request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("Yes form is valid")
            return HttpResponseRedirect(reverse('list'))
    else:
        # for field, errors in form.errors.items():
        # # Iterate over the errors for each field
        #     for error in errors:
        #         # Handle the error as needed
        #         print(f"Validation error for field '{field}': {error}")

        form = Courses_Form()
    return render (request, 'course.html', {'form': form})

# from django.views.generic import ListView
# from courses_section.models import CourseCategories
# class CourseCategories(ListView):
#     model = CourseCategories
#     template_name = 'CClist.html'

def history(request):
    return render(request, 'history.html')

from courses_section.models import Courses
def course_list(request):
    form = Courses.objects.all()
    return render(request, 'list.html' , {'form': form})

def delete_course(request, id):
    Courses.objects.filter(id=id).delete()
    form = Courses.objects.all()
    return render(request, 'list.html' , {'form': form})

def edit_course(request, id=None):
    if request.method == 'POST':
        print("I m inside Post method")
        edit = Courses.objects.get(id=id)
        fields = edit.__dict__.items()
        for f , v in fields:
            print(f , v)
        return HttpResponse("Data Not saved Successfully")

    else:
        print("I m inside get method")
        edit = Courses.objects.get(id=id)
        # fields = edit.__dict__.items()
        # empty_form_dict = {}
        # for column , value in fields:
        #     if column.startswith("_"):
        #         print(f'This is of no use thats why i used if block {column}{value}')
        #     empty_form_dict[column]= value

        # print(empty_form_dict)

        form = Courses_Form(instance=edit)
        
        print("form is sent")
        return render(request, 'edit.html', {'form':form})
    

def edit_it(request, id):
    a = Courses.objects.get(id=id)
    form = Courses.objects.all()
    return render(request, 'list.html' , {'form': form})


    