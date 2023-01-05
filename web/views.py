from django.shortcuts import render
from . models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.


def index(request):
    services= Services.objects.all()
    

    context = {
        'is_index': True,
        'service':services,
    }
    return render(request,'web/index.html',context)


def about(request):
    context = {
        'is_about': True,
    }
    return render(request,'web/about.html',context)
     

def contact(request):
    context = {
        'is_contact': True,
    }
    return render(request,'web/contact.html',context)



def myaccount(request):
    return render(request,'web/my-account.html')

def partner(request):
    return render(request,'web/partner-details.html')

def pricing(request):
    return render(request,'web/pricing.html')

def privacy(request):
    return render(request,'web/privacy-policy.html')

def register(request):
    return render(request,'web/register.html')

def requestquote(request):
    return render(request,'web/request-quote.html')

def servicedetails(request,id):
    services= Services.objects.get(id=id)

    context = {
        'service':services,
    }
    
    return render(request,'web/services-details.html',context)

def services(request):
    services= Services.objects.all()
    

    context = {
        'service':services,
        'is_services': True,
    }
    

    return render(request,'web/services.html',context)

def team(request):
    return render(request,'web/team.html')

def termsandconditions(request):
    return render(request,'web/terms-conditions.html')

def testimonials(request):
    return render(request,'web/testimonials.html')

def gallery(request):
    gallery= Gallery.objects.all()


    context = {

        'gallery':gallery,
        'is_gallery': True,


    }
    return render(request,'web/gallery.html',context)

def career(request):
    career= Career.objects.all()
    if request.method == 'POST':
        name = request.POST.get('clientname')
        email = request.POST.get('email')
        job = request.POST.get('client_contact_type')
        resume = request.POST.get('resume')
        career_data = CareerData(
            name = name,
            email = email,
            jobs = job,
            resume = resume
        )
        career_data.save()

    context = {

        'career':career,
        'is_career': True,
    }



    return render(request,'web/career.html',context)


@csrf_exempt
def message(request):
    name = request.POST['clientname']
    email = request.POST['email']
    phone = request.POST['clientPhone']
    subject = request.POST['subject']
    message = request.POST['message']

    if request.user is not None:
        try :
            number_obj = AdminNumber.objects.all().last()
            print(number_obj,"#"*10)
            number = number_obj.phone_number
        except :
            number = 0
    else :
        number = 0

    try:
        messagestring = 'https://wa.me/+91'+ number +'?text=Table Name :'+ name +\
                "%0a------------"
        
        
        messagestring +="%0aEmail:"+str(email)+"%0aPhone:"+str(phone)+"%0asubject:"+str(subject)+"%0amessage :"+str(message)+"%0a-----------------------------"
    except :
        messagestring = 'https://wa.me/+91?text=Table Name :'

    data = {
        "link":messagestring,
    }


    return JsonResponse(data)



@csrf_exempt
def message2(request):
    customer_name = request.POST['customer_name']
    customer_email = request.POST['customer_email']
    phone_number = request.POST['phone_number']
    msg_subject = request.POST['msg_subject']
    message = request.POST['message']

    if request.user is not None:
        print(request.user,"#"*10)
        number_obj = AdminNumber.objects.all().last()
        number = number_obj.phone_number
    else :
        number = 0

    try:
        messagestring = 'https://wa.me/+91'+ number +'?text=Table Name :'+ customer_name +\
                "%0a------------"
        print(messagestring)
        
        messagestring +="%0aEmail:"+str(customer_email)+"%0aphone-number:"+str(phone_number)+"%0asubject:"+str(msg_subject)+"%0amessage :"+str(message)+"%0a-----------------------------"
            
        
    except Exception as e:
        pass
    data = {
        "link":messagestring,
    }


    return JsonResponse(data)

def job_apply(request):
    if request.method == 'POST':
        name = request.POST.get('clientname')
        email = request.POST.get('email')
        job = request.POST.get('client_contact_type')
        resume = request.POST.get('resume')
        career_data = CareerData(
            name = name,
            email = email,
            jobs = job,
            resume = resume
        )
        career_data.save()
        print("Hello")
    return render(request,'web/career.html')