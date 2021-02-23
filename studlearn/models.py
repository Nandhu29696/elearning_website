from django.db import models
from datetime import datetime, date

# Create your models here.
class Userdeatils(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    useremail = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confpassword = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)

class Doubtqueryask(models.Model):
    studname = models.CharField(max_length=100)
    studemail = models.EmailField()
    studmobile = models.CharField(max_length=100)
    langdoubt = models.CharField(max_length=100)

class Coursedetails(models.Model): 
    courseimg= models.ImageField(upload_to='pics')  
    coursename = models.CharField(max_length=100)
    coursecontent = models.CharField(max_length=200)
    studententrollcount = models.CharField(max_length=100) 
    uploaddate = models.DateField(auto_now_add=False, auto_now=False, blank=True) 
    desccourse = models.TextField()
  
class Beginnercourses(models.Model):
    titlecourse = models.CharField(max_length=100)
    subtitlecourse = models.CharField(max_length=100)
    imgcourse= models.ImageField(upload_to='pics')  
    viewscourse = models.CharField(max_length=300)
    datecourse = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    daycourse = models.IntegerField()
    desccourse = models.TextField()
    offercourse = models.CharField(max_length=100, blank=True)
    pricecourse = models.IntegerField()
    courseauthor = models.CharField(max_length=100)  
    courseduration = models.CharField(max_length=100) 
    coursemode = models.CharField(max_length=100) 
     
class Intermediatecourses(models.Model):
    titlecourse = models.CharField(max_length=100) 
    subtitlecourse = models.CharField(max_length=100)
    imgcourse= models.ImageField(upload_to='pics')   
    viewscourse = models.CharField(max_length=300)
    datecourse = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    desccourse = models.TextField()
    offercourse = models.CharField(max_length=100, blank=True)
    pricecourse = models.IntegerField()
    courseauthor = models.CharField(max_length=100)  
    courseduration = models.CharField(max_length=100)
    coursemode = models.CharField(max_length=100)
 
class Professioncourses(models.Model):
    titlecourse = models.CharField(max_length=100)
    subtitlecourse = models.CharField(max_length=100)
    imgcourse= models.ImageField(upload_to='pics')  
    viewscourse = models.CharField(max_length=300)
    datecourse = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    desccourse = models.TextField()
    offercourse = models.CharField(max_length=100, blank=True)
    pricecourse = models.IntegerField()
    courseauthor = models.CharField(max_length=100)  
    courseduration = models.CharField(max_length=100)
    coursemode = models.CharField(max_length=100)
 
class Mastercourses(models.Model):
    titlecourse = models.CharField(max_length=100)
    subtitlecourse = models.CharField(max_length=100)
    imgcourse= models.ImageField(upload_to='pics')  
    viewscourse = models.CharField(max_length=300)
    datecourse = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    desccourse = models.TextField()
    offercourse = models.CharField(max_length=100, blank=True)
    pricecourse = models.IntegerField()
    courseauthor = models.CharField(max_length=100)  
    courseduration = models.CharField(max_length=100)
    coursemode = models.CharField(max_length=100)
 