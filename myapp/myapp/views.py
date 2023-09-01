from django.http import HttpResponse
from django.shortcuts import render
import  datetime
def home(request):
    # return HttpResponse("<h1>This is index page</h1>")
    j = request.POST['lopa']  # Retrieve the value of 'lopa' from the POST data
    print(j)  # Print the value of 'lopa'
    isActive=True
    name="Learning django"
    list_of_functions= [
        "WAF TO CHECK EVEN OR ODD",
        "WAF TO CHECK PRIME NUMBER",
        "WAF TO PRINT NUMBER FROM 1 TO 100",
        "WAF TO PRINT TRIANGLE"
    ]
    data={
        'isActive':isActive,
        'name':name,
        'list_of_functions':list_of_functions
    }
    return render(request,"home.html",data)

def about(request):
    # return  HttpResponse("<h1>About Page</h1>")
    return render(request,"about.html",{"Shubham":1,"Aman":2})

def service(request):
    # return  HttpResponse("<h1>Service Page</h1>")
    return  render(request,"service.html",{})