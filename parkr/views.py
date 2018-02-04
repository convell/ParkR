from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import EmailMessage, get_connection
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.sites.shortcuts import get_current_site
from django import forms
from .forms import PostForm, UserCreationFormEmail
from .models import parkingSpace
from .tokens import account_activation_token
import json

def index(request):
    latlngList=[]
    noteList=[]
    allObjects = parkingSpace.objects.all()
    for result in allObjects.values():
        #return HttpResponse(result)
        lat = result.get("lat")
        lng = result.get("lng")
        note = result.get("note")
        latlng = {"lat":float(lat),"lng":float(lng)}
        latlngList.append(latlng)
        noteList.append(note)
    jsonList = json.dumps(latlngList)
    noteList = json.dumps(noteList)

    if request.user.is_authenticated():
        username = request.user.username
    else:
        username = "NULL"
    return render(request, 'index.html', {"djangoMapMarkers":jsonList,"notes":noteList,"user":username})

def profile(request):
    username = None
    if request.user.is_authenticated():
        username = request.user
        ownedParkingSpaces = parkingSpace.objects.filter(owner=request.user.username)
        noteList = []
        for result in ownedParkingSpaces.values():
            note = result.get("note")
            noteList.append(note)
        if not noteList:
            noteList = "NULL"

    return render(request, 'profile.html', {"username":username, "noteList":noteList})

def reserve(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                formResponse =form.save(commit=False)
                formResponse.owner = request.user.username
                formResponse.save()
                return redirect('/')
    else:
        form = PostForm()
    return render(request, 'reserve.html',{'form':form})

def test(request):
    return render(request, 'test.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationFormEmail(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activate your Park'R account."
            message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            with get_connection() as connection:
                email = EmailMessage(
                        mail_subject, message, to=[to_email],connection=connection,
                )
                email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = UserCreationFormEmail()
    return render(request, 'signup.html', {'form': form})

def passwordChange(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request, 'your password was succesfully updated')
            return redirect('/accounts/profile')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'passwordChange.html', {'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
                    # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
