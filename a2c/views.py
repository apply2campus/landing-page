from django.shortcuts import render,redirect
from home.models import leads,newsletters, contact
from django.contrib import messages


def newsletter(request):
    if request.method == "POST":
        emails = request.POST.get('newsletter')
        obj, created = newsletters.objects.get_or_create(email=emails)
        if not created:
            print('Object already exists in the database')
            messages.success(request, 'Email Already Exits')
        else:
            obj.save()
            messages.success(request, 'Email submitted successfully.')
            return redirect('home')


def home(request):
    newsletter(request)
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('emailaddress')
        meetonline = request.POST.get('meet')
        visitoffice = request.POST.get('meet')
        date = request.POST.get('date')
        if name and email and date and ( meetonline or visitoffice):
            if meetonline:
                contact.objects.create(fullname=name,email=email,mode=meetonline,date=date)
            elif visitoffice:
                contact.objects.create(fullname=name,email=email,mode=visitoffice,date=date)
    return render(request,'index.html')

def forms(request):
    if request.method == "POST":
        destination = request.POST.get('Destination')
        yos = request.POST.get('Year-Of-Study')
        month = request.POST.get('Intake-Month')
        los = request.POST.get('level-of-study')
        los2 = request.POST.get('level-of-study2')
        firstname = request.POST.get('FirstName')        
        lastname = request.POST.get('LastName')        
        email = request.POST.get('Email') 
        phono = request.POST.get('PhoneNumber') 
        passport = request.POST.get('passport-with-validity-exceeding-6-months') 
        ept = request.POST.get('appeared-for-IELTS/TOEFL') 
        toe = request.POST.get('English-Proficiency-test') 
        Listing_Score = request.POST.get('EPT-Listing') 
        Reading_Score = request.POST.get('EPT-Reading') 
        Writing_Score = request.POST.get('EPT-Writing') 
        Speaking_Score = request.POST.get('EPT-Speaking') 
        Overall_Score = request.POST.get('EPT-Overall') 
        examname = request.POST.get('ExamName') 
        total_score = request.POST.get('OtherExamOverall') 
        fund = request.POST.get('fund-your-education') 
        budget = request.POST.get('approximate-budget') 
        tenp = request.POST.get('10th-Details-percentage') 
        tenpass = request.POST.get('10th-Details-yearPassing') 
        tenstate = request.POST.get('10th-Details-Board') 
        twep = request.POST.get('12th-Details-percentage') 
        twepass = request.POST.get('12th-Details-YearPassing') 
        twestate = request.POST.get('12th-Details-Board') 
        
        if destination and yos and month and firstname and lastname and email and phono:
            leads.objects.create(destination= destination, yos=yos, month=month, los=los, los2=los2, firstname=firstname,lastname=lastname, email=email,phono=phono , passport=passport, ept=ept, toe = toe, Listing_Score=Listing_Score, Reading_Score=Reading_Score, Writing_Score=Writing_Score,Speaking_Score=Speaking_Score, Overall_Score=Overall_Score, examname=examname,total_score=total_score,fund=fund,budget=budget ,tenp=tenp,tenpass=tenpass,tenstate=tenstate, twep=twep, twepass=twepass, twestate=twestate)
            
        return render(request,'success.html')
            
    return render(request,'form.html')


def blog1(request):
    return render(request,'blogs/blog1.html')
def blog2(request):
    return render(request,'blogs/blog2.html')
def blog3(request):
    return render(request,'blogs/blog3.html')