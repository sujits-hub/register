from django.shortcuts import render,HttpResponse
from home.models import Register

def index(request):
    return render(request,"register.html")

def submitForm(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        middle_name=request.POST['middle_name']
        last_name=request.POST['last_name']
        mobile_number=request.POST['mobile_number']
        collage_name=request.POST['collage_name']
        gender=request.POST['gender']
        programming=request.POST.get('programming','off')
        singing=request.POST.get('singing','off')
        dancing=request.POST.get('dancing','off')
        playing=request.POST.get('playing','off')
        hobbies=[]
        if programming=="programming":
           hobbies.append(programming)
        if singing=="singing":
           hobbies.append(singing)
        if dancing=="dancing":
           hobbies.append(dancing)
        if playing=="playing":
           hobbies.append(playing)
        Register(first_name=first_name,middle_name=middle_name,last_name=last_name,mobile_number=mobile_number,collage_name=collage_name,gender=gender,hobbies=hobbies).save()
        msg="Form Submited Successfully"
        return render(request,"register.html",{'msg':msg})
    else:
        return HttpResponse("404-not found")
