from django.shortcuts import render, redirect
from .models import Teacher, SubjectDetails
from .forms import  TeacherForm, SubjectForm, FileForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.core.files.base import ContentFile
from zipfile import ZipFile
import pandas as pd
from django.core.files.storage import FileSystemStorage


@login_required
def subjects(request):
    req = request.GET.get('search',None)
    if req is not None:
        query = request.GET.get('search')
        subject_details = SubjectDetails.objects.filter(Q(subject_name__icontains=query) )
    else:
        subject_details = SubjectDetails.objects.order_by("-date_created")
    return render(request,'teacher/subjects.html',{'subject_details':subject_details})

@login_required
def teachers(request):
    req = request.GET.get('search',None)
    if req is not None:
        query = request.GET.get('search')
        teachers = Teacher.objects.filter(
            Q(last_name__icontains=query) | 
            Q(subjectdetails__subject_name__icontains=query)
            ).order_by("-date_created")

    else:
        teachers = Teacher.objects.all().order_by("-date_created")
    return render(request,'teacher/teachers.html',{'teachers':teachers})

@login_required
def add_teacher(request):
    form = TeacherForm()
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/teachers')
    context = {'form':form}
    return render(request,"teacher/form_page.html",context)


@login_required
def upload_teachers(request):
    
    data = {}
    if "GET" == request.method:
        form = FileForm()
        context = {'form':form}
        return render(request,"teacher/upload_teachers.html",context)
    else:
        csv_file = request.FILES["teacher_file"]
        images_file = request.FILES["teacher_images"]
        zip_images = {}
        if not csv_file.name.endswith('.csv'):
            form = FileForm()
            messages.error(request,'File is not CSV type')
            context = {'form':form}
            return render(request,"teacher/upload_teachers.html",context)

        if not images_file.name.endswith('.zip'):
            form = FileForm()
            messages.error(request,'File is not ZIP type')
            context = {'form':form}
            return render(request,"teacher/upload_teachers.html",context)

        if images_file:
            zip_file = ZipFile(images_file)
            for name in zip_file.namelist():
                
                data = zip_file.read(name)
                zip_images[name.split('.')[0]] = data        

        if csv_file.multiple_chunks(): #if file is too large then return
            messages.error(request, 'Upload file is TOO big (%2f MB).' %(csv_file.size/(1000*1000),))
            form = FileForm()
            context = {'form':form}
            return render(request,"teacher/upload_teachers.html",context)
    
        fs = FileSystemStorage()
        file = fs.save('file_name.csv', csv_file)
        df = pd.read_csv(fs.path(file))
        for index, row in df.iterrows():
            try:
    
                data_dict = {}
                if row['Email Address']:
                    data_dict["first_name"] = row['First Name']
                    data_dict["last_name"] = row['Last Name']
                    data_dict["email"] = row['Email Address']
                    data_dict["phone"] = row['Phone Number']
                    data_dict["room_number"] = row['Room Number']
                    form = TeacherForm(data_dict)
                    if form.is_valid():
                        form.save()
                        if row['Profile picture'].split('.')[0] in zip_images.keys():
                            obj = Teacher.objects.get(email=row['Email Address'])
                            content_file = ContentFile(zip_images[row['Profile picture'].split('.')[0]])
                            obj.teacher_profile_pic.save('image_name.jpg', content_file)
                        my_list = [item for item in row['Subjects taught'].split(',') if item]
                        
                        for subject in my_list:
                            obj = Teacher.objects.get(email=row['Email Address'])
                            subject = subject.replace('"','')
                            subject_details = {}
                            subject_details['teacher'] = obj
                            subject_details['subject_name'] = subject
                            subjects_count = obj.subjectdetails_set.all().count()
                            
                            if int(subjects_count) <5:
                                form = SubjectForm(subject_details)
                                if form.is_valid():
                                    form.save()
                        
            except Exception as e:
                print('Exception occured during saving cutomer details' ,e)
        teachers = Teacher.objects.all()
        return render(request,'teacher/teachers.html',{'teachers':teachers}) 

@login_required
def update_teacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    form = TeacherForm(instance=teacher)
    if request.method == 'POST':
        form = TeacherForm(request.POST,request.FILES, instance=teacher)
        
        if form.is_valid():
            form.save()
            return redirect('/teachers')
    context = {'form': form}
    return render(request,'teacher/form_page.html',context)

@login_required
def delete_teacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    teacher.delete()
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def teacher_subjects(request, pk):
    teacher = Teacher.objects.get(id=pk)
    subject_details = teacher.subjectdetails_set.all()
    total_subjects = subject_details.count()
    context = {'teacher':teacher,'subject_details':subject_details, 'total_subjects':total_subjects}
    return render(request,'teacher/teacher_subjects.html', context)

@login_required
def create_subject(request):
    form = SubjectForm()
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/subjects')
    context = {'form':form}
    return render(request,'teacher/form_page.html', context)

@login_required
def update_subject(request, pk):
    order = SubjectDetails.objects.get(id=pk)
    form = SubjectForm(instance=order)
    if request.method == 'POST':
        form = SubjectForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/subjects')
    context = {'form': form}
    return render(request,'teahcer/form_page.html',context)
    
@login_required
def delete_subject(request, pk):
    order = SubjectDetails.objects.get(id=pk)
    order.delete()
    return redirect(request.META.get('HTTP_REFERER'))


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,"Username or Password is not correct.")
    return render(request, 'teacher/signin.html',{})

def signout(request):
    logout(request)
    return redirect('signin')