from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import Topic, WebPage, AccessRecord
from first_app.forms import FormName, UserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = { 'access_records': webpages_list }

    return render(request, "first_app/index.html", context=date_dict)

def contact(request):
    return HttpResponse("<em>Contact!</em>")

def form_page(request):
    form = FormName()
    if request.method == "POST":
        form = FormName(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])
    return render(request, 'first_app/form_page.html', { 'form': form })

def relative_page(request):
    return render(request, 'first_app/relative.html')

def other_page(request):
    return render(request, 'first_app/other.html')

def home(request):
    return render(request, 'first_app/home.html')

def registration(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'first_app/registration.html', {
    'user_form': user_form,
    'profile_form': profile_form,
    'registered': registered })

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('first_app:index'))
            else:
                return HttpResponse('Account not active')
        else:
            return HttpResponse('Failed login')
    else:
        return render(request, 'first_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:home'))
