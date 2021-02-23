from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Userdeatils, Coursedetails, Beginnercourses, Intermediatecourses, Professioncourses, Mastercourses, Doubtqueryask

#Create/save student detailed view page
def landingpage(request):
    if request.method == 'POST': 
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        useremail=request.POST['useremail']
        mobile=request.POST['mobile']
        password=request.POST['password']  
        confpassword=request.POST['confpassword']  
        # subtitle=request.POST['subtitle']
        if password == confpassword:
            user= Userdeatils.objects.create(firstname=firstname, lastname=lastname, useremail=useremail, mobile=mobile, password=password, confpassword=confpassword)
            user.save()
            return render(request, 'index.html', {'firstname':firstname})
        else: 
            messages.info(request, 'password not match')
    return render(request, 'landingpage.html') 
  
#Student Login page view
def landlogin(request):
    
    if request.method == 'POST': 
        useremail = request.POST['useremail']
        password = request.POST['password']
        try:
            user = Userdeatils.objects.get(useremail=useremail, password=password) 
            context = {
                'firstname' : user.firstname,
                'lastname' : user.lastname
            }
            return render(request, 'index.html', context)  
        except:
            messages.info(request, 'invalid credentials')
            return render(request, 'landingpage.html')
       
    return render(request, 'landingpage.html')     

#Index page view
def indexpage(request):

    return render(request, 'index.html')

#Student Course query details saved using call function
def coursestudquery(request): 
    if request.method == 'POST': 
        studname=request.POST['studname']
        studemail=request.POST['studemail'] 
        studmobile=request.POST['studmobile'] 
        langdoubt=request.POST['langdoubt']  
        studquery= Doubtqueryask.objects.create(studname=studname, studemail=studemail, studmobile=studmobile, langdoubt=langdoubt)
        studquery.save()

#beginner 1 month courses view
def begincourse(request):
    coursestudquery(request) #Function called
    bc = Beginnercourses.objects.all()
    return render(request, 'beginner_course_view.html', {'bc':bc})  

#Intermediate 3 month courses view
def intermediatecourse(request): 
    coursestudquery(request) #Function called
    ic = Intermediatecourses.objects.all()
    return render(request, 'intermediate_course_view.html', {'ic':ic})  
 
#Profession 6 month courses view
def professioncourse(request): 
    coursestudquery(request) #Function called
    pc = Professioncourses.objects.all()
    return render(request, 'profession_course_view.html', {'pc':pc})  

#Master 1 year courses view
def mastercourse(request): 
    coursestudquery(request) #Function called
    mc = Mastercourses.objects.all()
    return render(request, 'master_course_view.html', {'mc':mc})     
 
#Beginner course details view 
def courseview(request, id):  
    try:
        if begincourse(request):
            obj=Beginnercourses.objects.get(pk=id)    
            context = {
                'titlecourse'    : obj.titlecourse,
                'subtitlecourse' : obj.subtitlecourse,
                'imgcourse'      : obj.imgcourse,
                'viewscourse'    : obj.viewscourse,
                'datecourse'     : obj.datecourse,
                'desccourse'     : obj.desccourse, 
                'offercourse'    : obj.offercourse, 
                'courseauthor'   : obj.courseauthor 
            }
            return render(request, 'course_detail_view.html', context)
    except: 
        raise Exception("Course not shown...")
    
#Intermediate course details view 
def intercourseview(request, id): 
    try: 
        vas = Intermediatecourses.objects.get(pk=id)
        context = {
        'titlecourse' : vas.titlecourse,
        'subtitlecourse' : vas.subtitlecourse,
        'imgcourse' : vas.imgcourse,
        'viewscourse' : vas.viewscourse,
        'datecourse' : vas.datecourse,
        'desccourse' : vas.desccourse,
        'offercourse' : vas.offercourse,
        'courseauthor' : vas.courseauthor
        }
        return render(request, 'intermediate_course_detail_view.html', context) 
    except:
         raise Exception("Course not shown...")

