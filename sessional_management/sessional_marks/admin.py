from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

# admin.site.register(item)
@admin.register(Student_first_year,Student_second_year,Student_third_year,Student_fourth_year,Teacher_data)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )

class Student_first_yearAdmin(admin.ModelAdmin):
    # list_display = ['id','sstudent_name','srollno','sbranch','sfirst_marks','ssecond_marks','sthird_marks','stotal_marks']
    pass

class Student_second_yearAdmin(admin.ModelAdmin):
    # list_display = ['id','sstudent_name','srollno','sbranch','sfirst_marks','ssecond_marks','sthird_marks','stotal_marks']
    pass


class Student_third_yearAdmin(admin.ModelAdmin):
    # list_display = ['id','sstudent_name','srollno','sbranch','sfirst_marks','ssecond_marks','sthird_marks','stotal_marks']
    pass

class Student_fourth_yearAdmin(admin.ModelAdmin):
    # list_display = ['id','sstudent_name','srollno','sbranch','sfirst_marks','ssecond_marks','sthird_marks','stotal_marks']
    pass

class Teacher_dataAdmin(admin.ModelAdmin):
    list_display = ['id','tteacher_name','tteacher_branch']
"""
# admin.site.register(item)
# @admin.register(Student_first_year,Student_second_year,Student_third_year,Student_fourth_year,Teacher_data)
@admin.site.register(Student_first_year,Student_first_yearAdmin)
@admin.site.register(Student_second_year,Student_second_yearAdmin)
@admin.site.register(Student_third_year,Student_third_yearAdmin)
@admin.site.register(Student_fourth_year,Student_fourth_yearAdmin)
@admin.site.register(Teacher_data,Teacher_dataAdmin)
"""