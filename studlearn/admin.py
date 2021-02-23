from django.contrib import admin
from .models import Coursedetails, Beginnercourses, Intermediatecourses, Professioncourses, Mastercourses

# Register your models here.

admin.site.register(Coursedetails)
admin.site.register(Beginnercourses)
admin.site.register(Intermediatecourses)
admin.site.register(Professioncourses)
admin.site.register(Mastercourses)  