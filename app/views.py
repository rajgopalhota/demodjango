from django.http import HttpResponse
from django.shortcuts import render

from . import  models


def home(req):
    return HttpResponse("Home")

def addstu(req):
    if req.method == "POST":

        name = req.POST.get('name')
        age = req.POST.get('age')
        grade = req.POST.get('grade')

        # Create a new student object with the received data
        new_student = models.Student(name=name, age=age, grade=grade)
        # Save the new student object to the database
        new_student.save()

        # Redirect to some page or render a success message
        return render(req, 'add.html')

    return render(req, 'add.html')

def view(req):
    students = models.Student.objects.all()
    # Pass the list of students to the template context
    return render(req, 'view.html', {'students': students})
    # return render(req, 'view.html')