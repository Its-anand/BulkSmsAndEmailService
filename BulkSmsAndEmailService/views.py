from django.http import HttpResponse
from django.shortcuts import render 
def homePage(request):
    return render(request,"index.html")


# email sending code----------------------------------------
import smtplib as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as p
from django.contrib import messages
import email,email.encoders,email.mime.text,email.mime.base
def sendemail(request):
    if request.method == "POST":
        
        try:
            #get data from html page to backend
           sub=request.POST['subject']
           msg=request.POST['sms']
            #read excel file 
           file=request.FILES['e-file']
           print("uploaded file is ",file)
            
            #file='C:/Users/lenovo/Desktop/email/email/Email.xlsx'
           data=p.read_excel(file)
           print(type(data))
           email_col=data.get("email")
           list_email=list(email_col)
           print(list_email)
           #sending email process
           sender="dikshakushwah17@gmail.com"
           password="sficbljvbeyyybgz"
           reciver=list_email
           message=MIMEMultipart()
           message['subject']=sub
           body=msg
           

           server=sm.SMTP("smtp.gmail.com",587)
           server.starttls()
           server.login(sender,password)
           
           text=MIMEText(body, 'plain')

           
           message.attach(text)
           server.sendmail(sender,reciver,message.as_string())
           messages.success(request, 'success')
           return render(request,"index.html")
        except Exception as e:
            #return render(request,"index.html")
            messages.error(request, 'error')
            return render(request,"index.html")
        
    else:
        return render(request,"email.html")

# whatsaap msg  sending code----------------------------------------

from twilio.rest import Client 
 
def sendwhatsapp(request):
    if request.method == "POST":
      msg=request.POST['sms']
      #file=request.POST['w-file']
      account_sid = 'ACd9758550b7b1602e06f6ccefe38ff760' 
      auth_token = '2d3535e80d045232868375cee13e4849' 
      client = Client(account_sid, auth_token) 
    
      message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body=msg,      
                                    to='whatsapp:+917049011575' 
      )
      
      print(message.sid)
      messages.success(request, 'success')                      
      return render(request,"index.html") 
      
    else:
        messages.error(request, 'error')
        return render(request,"whatsapp.html")



def sms(request):#c03d9c00d04e5c786ca118c0f43cf64e6ce8fe244168f80cd097197bb283315a
        return render(request,"sms.html")