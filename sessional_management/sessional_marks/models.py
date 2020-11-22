from django.db import models
from sessional_marks.models import models
# Create your models here.

# data of first year student
class Student_table(models.Model):
    sstudent_name = models.CharField(max_length = 100)
    srollno = models.CharField(max_length = 12, blank = False)
    sbranch = models.CharField(max_length = 10)
    sfirst_marks = models.IntegerField()
    ssecond_marks = models.IntegerField()
    sthird_marks = models.IntegerField()
    stotal_marks = models.IntegerField()
    
    class Meta:
        abstract = True

    def __str__(self):
        return 'Rollno : {0} Branch : {1}'.format(self.srollno, self.sbranch)

    

class Student_first_year(Student_table):
    class Meta:
        db_table = "student_first_year"

class Student_second_year(Student_table):
    class Meta:
        db_table = "student_second_year"

class Student_third_year(Student_table):
    class Meta:
        db_table = "student_third_year"
    

class Student_fourth_year(Student_table):
    class Meta:
        db_table = "student_fourth_year"

class Teacher_data(models.Model):
    tteacher_name = models.CharField(max_length =20)
    tteacher_branch = models.CharField(max_length = 10)
    tteacher_email = models.EmailField(max_length = 100)
    tteacher_mob = models.CharField(max_length = 12)
    tteacher_userid = models.CharField(max_length = 20)
    tteacher_password = models.CharField(max_length = 10)

    class Meta:
        db_table = "Teacher_data"

    def __str__(self):
        return self.tteacher_name