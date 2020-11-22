from django.shortcuts import render,redirect
from .models import *
from .forms import *


# Create your views here.
def add_new(request):
    if request.method == "POST":
        form = Student1Form(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show/")
            except:
                pass
    else:
        form = Student1Form()
    return render(request,"display/new_student.html",{'form':form})


def teacher_sign_in(request):
    if request.method == "POST":
        return render(request,"/teacher_home")

def teacher_home(request):
    teacher_record = Teacher_data.objects.all()
    return render(request,"display/teacher_home.html",{'teacher_record':teacher_record})

def index(request):
    return render(request,"display/index.html")

def teacher_registration(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/teacher_home/")
            except:
                pass
    else:
        form = TeacherForm()
    return render(request,"display/teacher_registration.html",{'form':form})   

def show(request):
    student_first_record = Student_first_year.objects.all()
    return render(request,"display/show.html",{'student_record':student_first_record})

def delete(request, id):
    student_record = Student_first_year.objects.get(id = id)
    student_record.delete()
    return redirect("/show/")


# def edit(request, id):
#     student_record = Student_first_year.objects.get(id = id)
#     return render(request,"display/edit.html",{'student_record':student_record})

# def update(request, id):
#     student_record = Student_first_year.objects.get(id = id)
#     form = Student1Form(request.POST, instance = student_record)
#     if form.is_valid:
#         form.save()
#         return redirect("/show/")

#     return render(request,"display/edit.html",{'student_record':student_record})






#----------------------------------------------------------------------------------------------------------------

"""

def index(request):
    return HttpResponseRedirect(reverse('employee_list'))

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return HttpResponseRedirect(reverse('employee_list'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "auth/login.html", context)
    else:
        return render(request, "auth/login.html", context)

@login_required(login_url="/login/")
def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "auth/success.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))



"""