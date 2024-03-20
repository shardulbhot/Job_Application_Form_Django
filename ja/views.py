from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

def index(req):

    if req.method=='POST':
        form=ApplicationForm(req.POST)
        if form.is_valid():
            fname=form.cleaned_data["first_name"]
            lname=form.cleaned_data["last_name"]
            em=form.cleaned_data["email"]
            df=form.cleaned_data["date_from"]
            occp=form.cleaned_data["occupation"]

            Form.objects.create(first_name=fname,last_name=lname,email=em,
                                date_from=df,occupation=occp)

            message_body = """Jaycha ka round la @ {} 
                    """.format(fname)
            em_msg=EmailMessage("Jaycha ka Round la",message_body,to=[em])
            em_msg.send()

            messages.success(req,"{} ,Your form was submitted successfully".format(fname))


    return render(req,"index.html")

def about(req):
    return render(req,"about.html")