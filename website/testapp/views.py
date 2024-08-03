from django.shortcuts import render

# Create your views here.
def check(request):
    return render(request,'main.html')
def staff(request):
    return render(request,'staff.html')
def student(request):
    return render(request,'student.html')
def event(request):
    return render(request,'Event.html')