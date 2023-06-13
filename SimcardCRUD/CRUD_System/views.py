from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import TariffPlan, Simcard

from .forms import *

# Create your views here.


@login_required(login_url='login-request')
def main(request):

    if request.method == "GET":
        if "deleted-record-id" in request.GET:
            Simcard.objects.filter(pk=request.GET.get('deleted-record-id')).delete()

            return redirect('/')

        elif "add-record-IMEI" in request.GET:
            current_tariff = TariffPlan.objects.filter(Title=request.GET.get("add-record-ServiceType"))

            SimcardRecord = Simcard(IMEI=request.GET.get('add-record-IMEI'),
                                    PhoneNumber=request.GET.get('add-record-Phone'),
                                    ClientName=request.GET.get("add-record-CustomerName"),
                                    RegistrationDate=request.GET.get("add-record-RegDate"),
                                    TariffPlan=current_tariff[0])

            SimcardRecord.save()
            print(request.GET)

            return redirect('/')

        elif "update-record-IMEI" in request.GET:

            current_tariff = TariffPlan.objects.filter(pk=request.GET.get("update-record-ServiceType-pk"))

            current_simcard_record = Simcard.objects.get(id=request.GET.get('update-record-simcard-pk'))

            current_simcard_record.IMEI = request.GET.get('update-record-IMEI')
            current_simcard_record.PhoneNumber = request.GET.get('update-record-Phone')
            current_simcard_record.ClientName = request.GET.get('update-record-CustomerName')
            current_simcard_record.RegistrationDate = request.GET.get('update-record-RegDate')
            current_simcard_record.TariffPlan = current_tariff[0]

            current_simcard_record.save()

            print(request.GET)

            return redirect('/')

    context = {"Simcards": Simcard.objects.all(),
               "TariffPlan": TariffPlan.objects.all()}

    return render(request, "CRUD_System/Simcard_CRUD.html", context=context)


def login_request(request):

    if request.method == "POST":
        form = CRUDSystemLoginForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print('works', request.POST)
            username = form.cleaned_data.get('Username')
            password = form.cleaned_data.get('Password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print('authenticated successfully!')
                login(request, user)

                return redirect("/")
            else:
                messages.error(request, "Неверно введены имя и/или пароль", extra_tags="message-box-login-error")
        else:
            messages.error(request, "Неверно введены имя и/или пароль", extra_tags="message-box-login-error")

    context = {"CRUDSystemLoginForm": CRUDSystemLoginForm}

    return render(request, "CRUD_System/Simcard_CRUD_login.html", context=context)


def logout_request(request):
    logout(request)

    return redirect('/')

