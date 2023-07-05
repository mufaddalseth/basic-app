from django.db import models
import os

# Create your models here.
"""
In OOPS a popular design pattern is MVC which is given by Gang of 4 (Read in future).

MVC -    M -Model (Structure / Prototype) 
         V - View (present the data)
         C - Controller (Receiving the request / calculations)
         In django instead of C we have T - template
 work on theroy of seperation of concerns
What is the diffrence between MVC and MVT????
What is difference between __new__ and __init__ while defining function??

Imp Notes
ORM - Object Relational Mapper.
It is a library by which a developer do not repeat the code.

Many type of databases are there RDBMS, Graph database (use by fb) , mongo db etc

IN ORM -  A real life Object to database mapping can be done by which a table in DBMS will be here a class.
Table = Class
Column = Object 
Table column = class Data



Programming paradigm
1. Sequential Programming
2. Functional Programming
3. Object oriented Programming

IN Django there is shell - To communicate with the DB server

Django ORM commands

class.objects.all()

Makemigrations - To create a table from model
sqlmigrate - To see the sql code after makemigrations and before the migrate
migrate - Save and complete the table in database

While creating a data it will automatically adds a ID Column to the table.
What are the need of mandotary ID column?

"""


class Courses(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    application = models.CharField(max_length=250 , default=None)
    fees = models.PositiveIntegerField(default=None)
    DURATION_CHOICES = [
        ('1 Month','1 Month'),
        ('2 Months','2 Months'),
        ('3 Months','3 Months'),
        ('6 Months','6 Months'),
        ('9 Months','9 Months'),
    ]
    duration = models.CharField(max_length=20 , choices=DURATION_CHOICES, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='courses_section/images', default='')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'bignalytics_courses'
        ordering = ['name']

class CourseCategories(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name