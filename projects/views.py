from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id':'1',
        'title':"Ecommerce website",
        'description':'fully automated ecommerce site'
    },
    {
        'id':'2',
        'title':"Self profile website",
        'description':'help you to find a tasty job'
    },
    {
        'id':'3',
        'title':"Problem Solving webite",
        'description':'attach your problem, and you may get through'
        },
]


def projects(request):
    page = 'projects'
    number = 8
    context = {'page':page, 'number':number, 'projects':projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i

    return render(request, 'projects/single-project.html', {'project':projectObj})


