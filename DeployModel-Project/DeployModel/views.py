from django.http import HttpResponse
from django.shortcuts import render
import joblib

def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def result(request):

    cls = joblib.load('finalized_model.sav')

    lis = []

    lis.append(request.GET['Age'])
    lis.append(request.GET['Male'])
    lis.append(request.GET['Female'])
    lis.append(request.GET['ECE'])
    lis.append(request.GET['CSE'])
    lis.append(request.GET['IT'])
    lis.append(request.GET['MECH'])
    lis.append(request.GET['EEE'])
    lis.append(request.GET['CIVIL'])
    lis.append(request.GET['Internships'])
    lis.append(request.GET['CGPA'])
    lis.append(request.GET['Hostel'])
    lis.append(request.GET['Backlogs'])

    print(lis)

    ans = cls.predict([lis])
    if request.method == 'GET':
        return render(request,'result.html',{'ans':ans,'lis':lis})
