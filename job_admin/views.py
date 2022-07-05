from django.shortcuts import render

# Create your views here.

def user_login(request):
    return render(request,'emp/login.html')
def view_emp(request):
    return render(request,'emp/view employees.html')


