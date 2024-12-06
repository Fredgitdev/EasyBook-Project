from urllib import request
from django.shortcuts import render,redirect
from django.contrib import messages  # Import the messages framework

from easybookapp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from easybookapp.models import OneWayBooking, BusHiring, Contact, Member, ImageModel
from easybookapp.forms import OneWayBookingForm, BusHiringForm, ImageUploadForm
import requests
import json
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse


# Create your views here.

def index(request):              #when redirected to login
    if request.method == 'POST': #get to username and password to check if they exist
        if Member.objects.filter(
                username=request.POST['username'],
                password=request.POST['password'],
        ).exists():             #after confirming they exist by fetching
            members = Member.objects.get(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            return render(request, 'index.html', {'members': members})

        else:
            return render(request, 'pages-login.html')
    else:
        return render(request, 'pages-login.html')


def pagesblank(request):
    return render(request, 'pages-blank.html')

def pagescontact(request):
    if request.method == 'POST':
        mycontact=Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        messages.success(request, 'Your message has been saved..')
        return redirect('/contactshow')
    else:
        return render(request, 'pages-contact.html')



def pagesfaq(request):
    return render(request, 'pages-faq.html')

def pageslogin(request):
    return render(request, 'pages-login.html')

def pagesregister(request):
    if request.method == "POST":
        members = Member(
            name=request.POST['name'],
            email=request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password']
        )
        members.save()
        return redirect('/pages-login')
    else:
        return render(request, 'pages-register.html')



def tablesdata(request):
    return render(request, 'tables-data.html')

def tablesgeneral(request):
    return render(request, 'tables-general.html')

def contactshow(request):
    allcontacts = Contact.objects.all() # Fetch all contacts from the database
    return render(request, 'contactshow.html', {'contacts':allcontacts}) # Pass data to the template


def usersprofile(request):
    return render(request, 'users-profile.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def oneway(request):
    if request.method == "POST":
        myonewaybooking=OneWayBooking(full_name=request.POST['fullName'],
                      from_location=request.POST['fromLocation'],
                      to_location=request.POST['toLocation'],
                      departure_date=request.POST['departureDate'],
                      departure_time=request.POST['departureTime'],
                      number_of_seats=request.POST['numberOfSeats'],
        )
        myonewaybooking.save()
        messages.success(request, 'Your one-way booking has been submitted successfully!')
        return redirect('/onewayconfirmation')

    else:
        return render(request, 'oneway.html')




def hire(request):
    if request.method == "POST":
        mybushiring=BusHiring(full_name=request.POST['hireFullName'],
                  pick_up_location=request.POST['pickUpLocation'],
                  drop_off_location=request.POST['dropOffLocation'],
                  pick_up_date=request.POST['pickUpDate'],
                  pick_up_time=request.POST['pickUpTime'],
                  contact=request.POST['contact'],
                  bus_type=request.POST['busType'],
                  seat_capacity=request.POST['seatCapacity'],
        )
        mybushiring.save()
        messages.success(request, 'Your Bus Hire booking has been submitted successfully!')
        return redirect('/bushireconfirmation')

    else:
        return render(request, 'hire.html')



def onewayconfirmation(request):
    allonewaybookings = OneWayBooking.objects.all() #Fetch all One-Way Bookings
    return render(request, 'onewayconfirmation.html', {'oneway_bookings': allonewaybookings}) # Pass data to template



#Deleting Oneway records by a user
# def delete(request,id):
#     one_way_booking=OneWayBooking.objects.get(id=id)
#     one_way_booking.delete()
#     messages.success(request, 'Your One-way booking has been deleted successfully!')
#     return redirect('/onewayconfirmation')

def delete_oneway(request, id):
    one_way_booking = OneWayBooking.objects.get(id=id)
    one_way_booking.delete()
    messages.success(request, 'Your One-way booking has been deleted successfully!')
    return redirect('/onewayconfirmation')

def delete_bushire(request, id):
    bus_hiring_booking = BusHiring.objects.get(id=id)
    bus_hiring_booking.delete()
    messages.success(request, 'Your Bus Hiring booking has been deleted successfully!')
    return redirect('/bushireconfirmation')

def bushireconfirmation(request):
    allbushirebookings = BusHiring.objects.all() #Fetch all Bus Hiring records
    return render(request, 'bushireconfirmation.html', {'bushiring_bookings': allbushirebookings}) # Pass data to template



#Deleting Bus Hiring records by a user
# def delete(request,id):
#     bus_hiring_booking=BusHiring.objects.get(id=id)
#     bus_hiring_booking.delete()
#     messages.success(request, 'Your Bus Hiring booking has been deleted successfully!')
#     return redirect('/bushireconfirmation')



#Function to render Onewaybooking.html
def onewayedit(request,id):
    editonewaybooking=OneWayBooking.objects.get(id=id)
    return render(request,'onewayedit.html', {'oneway_bookings': editonewaybooking})

#Function to render Bushirebooking.html
def bushireedit(request,id):
    editbushiringbooking=BusHiring.objects.get(id=id)
    return render(request, 'bushireedit.html', {'bushiring_bookings': editbushiringbooking})



# def update(request,id):
#     updateinfo=OneWayBooking.objects.get(id=id)
#     form = OneWayBookingForm(request.POST, instance=updateinfo)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Your One-way booking has been updated successfully!')
#         return redirect('/onewayconfirmation')
#     else:
#         return render(request,'onewayedit.html')
#

def update_oneway(request, id):
    updateinfo = OneWayBooking.objects.get(id=id)
    form = OneWayBookingForm(request.POST, instance=updateinfo)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your One-way booking has been updated successfully!')
        return redirect('/onewayconfirmation')
    else:
        return render(request, 'onewayedit.html')

def update(request,id):
    updateinfo1=BusHiring.objects.get(id=id)
    form = BusHiringForm(request.POST, instance=updateinfo1)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your BusHiring has been updated successfully!')
        return redirect('/bushireconfirmation')
    else:
        return render(request,'bushireedit.html')



def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')

def token(request):
    consumer_key = 'MmYSwOHBcvphM7XoZWqzaBqLKhE4EVrUHF1AsmjriyzYZig5'
    consumer_secret = 'l99RBJGbyKuM8TNPlgnnAGzZkC5uTFtJImP3DCYyynD2JKEVLGGqTy4fL92MW2sZ'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "EasyBook",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")