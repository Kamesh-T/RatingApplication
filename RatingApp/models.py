from django.db import models

# Create your models here.
class RatingTable(models.Model):

    Name = models.CharField(max_length=15,primary_key=True)
    rValue=[
        ('1','1'),('2','2'),('3','3'),('4','4'),('5','5')
    ]
    project1 = models.CharField(max_length=2,choices=rValue,help_text='Generating strong password using python')
    project2 = models.CharField(max_length=2,choices=rValue,help_text='Children vaccination management using python')
    project3 = models.CharField(max_length=2,choices=rValue,help_text='Traffic prediction using python')
    project4 = models.CharField(max_length=2,choices=rValue,help_text='Webdevelopment using HTML,Css,Py,PostgreSQL')
    project5 = models.CharField(max_length=2,choices=rValue,help_text='Medcare development using python')
    project6 = models.CharField(max_length=2,choices=rValue,help_text='Calculator App using python')
    project7 = models.CharField(max_length=2,choices=rValue,help_text='Logic Game using python')
    project8 = models.CharField(max_length=2,choices=rValue,help_text='Schedule Messenger using python')
    project9 = models.CharField(max_length=2,choices=rValue,help_text='Housing Society Management System using Java')
    project10 = models.CharField(max_length=2,choices=rValue,help_text='Emergency Service Locator using python')
    project11 = models.CharField(max_length=2,choices=rValue,help_text='Develop the English Knowledge of Children using python')
    project12 = models.CharField(max_length=2,choices=rValue,help_text='Virtual Drivers using Python')
    project13 = models.CharField(max_length=2,choices=rValue,help_text='Portfolio Management using Py,Html')
    project14 = models.CharField(max_length=2,choices=rValue,help_text='Chatbot development using Python')
    project15 = models.CharField(max_length=2,choices=rValue,help_text='Language Translator using Java')
    project16 = models.CharField(max_length=2,choices=rValue,help_text='Online voting System using Python')
    project17= models.CharField(max_length=2,choices=rValue,help_text='Route Analysis using Python')
    project18 = models.CharField(max_length=2,choices=rValue,help_text='Converting Text to audio & Audio to text using python')
    project19 = models.CharField(max_length=2,choices=rValue,help_text='Facemask Detection using python')
    project20 = models.CharField(max_length=2,choices=rValue,help_text='Incident Reporter using Python')
    project21 = models.CharField(max_length=2,choices=rValue,help_text="Tracks of people's Creditscores & Dues using Python")
    # project22 = models.CharField(max_length=2,choices=rValue,help_text='')
    # project23= models.CharField(max_length=2,choices=rValue,help_text='')
    # project24= models.CharField(max_length=2,choices=rValue,help_text='')
    # project25= models.CharField(max_length=2,choices=rValue,help_text='')
    # project26= models.CharField(max_length=2,choices=rValue,help_text='')
    # project27= models.CharField(max_length=2,choices=rValue,help_text='')
    # project28= models.CharField(max_length=2,choices=rValue,help_text='')
    # project29= models.CharField(max_length=2,choices=rValue,help_text='')
    # project30= models.CharField(max_length=2,choices=rValue,help_text='')

