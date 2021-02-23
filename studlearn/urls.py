from django.urls import path
from studlearn import views

urlpatterns = [
    path('landingpage', views.landingpage, name="landingpage"),
    path('', views.landlogin, name="landlogin"),
    path('courseview/<int:id>/',views.courseview, name="courseview"),
    path('intercourseview/<int:id>/',views.intercourseview, name="intercourseview"), 
    path('begincourse', views.begincourse, name="begincourse"), 
    path('intermediatecourse', views.intermediatecourse, name="intermediatecourse"), 
    path('professioncourse', views.professioncourse, name="professioncourse"), 
    path('mastercourse', views.mastercourse, name="mastercourse"),  
]      