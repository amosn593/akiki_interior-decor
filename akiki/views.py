from django.shortcuts import render, redirect
from .models import *
from django.utils.datetime_safe import datetime
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail

# Create your views here.

#Index page
def index(request):
    return render(request, 'akiki/index/index.html')


#Contact us page
def contact(request):
    return render(request, 'akiki/contact/contact.html')

# ajax_posting function
def ajax_posting(request):
    if request.is_ajax():
        full_name = request.POST.get('full_name').strip()
        phone = request.POST.get('phone')
        mail = request.POST.get('mail').strip()
        msg = request.POST.get('msg').strip()
        if full_name != '' and phone != '' and mail != '' and msg != '':
            subject = f"Client Message - {full_name} - {phone}"
            message= f"Thank you for Contacting Akiki Interio\n\nName: {full_name}\n\nPhone: {phone}\n\nEmail: {mail}\n\nMessage: {msg}\n\n\n\nAkiki Interior and Decor\n0705935996\nakikiinterior@gmail.com\n\nBringing Decor to You!"
            try:
                send_mail(subject,message,'akikiinterior@gmail.com',
                [mail, 'akikiinterior@gmail.com'],
                fail_silently=False,
                )
                response = {
                'msg':'Your message has been submitted successfully',
                    }
                return JsonResponse(response, safe=False)
            except:
                response = {
                'msg':'Check Your internet connection and try again!!!',
                    }
                return JsonResponse(response, safe=False)
        else:
            response = {
                'msg':'Fill all required Fields!!!',
            }
            return JsonResponse(response, safe=False)
    return HttpResponse("INVALID URL!!!")


#Services page
def services(request):
    return render(request, 'akiki/services/services.html')

#Gallery page
def gallery(request):
    return render(request, 'akiki/gallery/gallery.html')

