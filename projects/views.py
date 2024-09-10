from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm, ReviewForm
from django.contrib import messages


def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method =='POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.voteCount
        messages.success(request, "comment success")

    return render(request, 'projects/single-project.html', {'project':projectObj, 'form':form})

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            messages.success(request, "create project successfully")
            return redirect('projects')


    context = {'form':form}
    return render(request, 'projects/project_form.html', context)


def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid():
            form.save()
            messages.success(request, "update project successfully")
            return redirect('projects')


    context = {'form':form}
    return render(request, 'projects/project_form.html', context)

def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    context = {'object':project}

    if request.method=='POST':
        project.delete()
        messages.success(request, "delete project successfully")
        return redirect('projects')
    return render(request, 'delete_template.html', context)

