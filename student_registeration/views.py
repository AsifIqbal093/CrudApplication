from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import StudentInfo

# Create your views here.

def student_list(request):
    contex = {'student_list':StudentInfo.objects.all()}
    return render(request, 'student_registeration/student_list.html', contex)

def student_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            form = StudentForm()
        else:
            student = StudentInfo.objects.get(pk=id)
            form = StudentForm(instance=student)
        return render(request, 'student_registeration/student_form.html', {'form':form})
    else:
        if id==0:
            form = StudentForm(request.POST)
        else:
            student = StudentInfo.objects.get(pk=id)
            form = StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('/student/list')

def student_delete(request, id):
    student = StudentInfo.objects.get(pk=id)
    student.delete()
    return redirect('/student/list')
