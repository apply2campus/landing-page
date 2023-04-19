from django.db import models


class newsletters(models.Model):
    email = models.EmailField(("Email"), max_length=254,null=True,blank=True)

    def __str__(self):
        return self.email
    
class contact(models.Model):
    fullname =models.CharField(("Fullname"), max_length=250)
    email = models.CharField(("Email"), max_length=250)
    mode = models.CharField(("Mode"), max_length=50)
    date = models.DateField(("Date"), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.fullname
    

class leads(models.Model):
    destination = models.CharField(("Destination"), max_length=150)
    yos = models.CharField(("Year of Study"), max_length=50)
    month = models.CharField(("Year of Month"), max_length=150)
    los = models.CharField(("level of study"), max_length=150)
    los2 = models.CharField(("level of study"), max_length=150)
    firstname = models.CharField(("First Name"), max_length=150)
    lastname = models.CharField(("Last Name"), max_length=150)
    email = models.CharField(("Email"), max_length=250)
    phono = models.CharField(("Phone Number"), max_length=150)
    passport = models.CharField(("Passport"), max_length=150)
    ept = models.CharField(("Have you appeared for IELTS/TOEFL or any English proficiency test?"), max_length=50)
    toe = models.CharField(("Type of Exam"), max_length=50)
    Listing_Score = models.CharField(("Listing_Score"), max_length=150)
    Reading_Score = models.CharField(("Reading_Score"), max_length=150)
    Writing_Score = models.CharField(("Writing_Score"), max_length=150)
    Speaking_Score = models.CharField(("Speaking_Score"), max_length=150)
    Overall_Score = models.CharField(("Overall_Score"), max_length=150)
    examname = models.CharField(("Exam Name"), max_length=150)
    total_score = models.CharField(("Total Score"), max_length=150)
    fund = models.CharField(("Fund"), max_length=150)
    budget = models.CharField(("Budget"), max_length=150)
    tenp = models.CharField(("10TH Percentage"), max_length=150)
    tenpass = models.CharField(("10th Passing"), max_length=150)
    tenstate = models.CharField(("Syllabus"), max_length=150)
    twep = models.CharField(("12TH Percentage"), max_length=150)
    twepass = models.CharField(("12th Passing"), max_length=150)
    twestate = models.CharField(("Syllabus"), max_length=150)

    def __str__(self):
        return self.firstname + self.lastname 
    