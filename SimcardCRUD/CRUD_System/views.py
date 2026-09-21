from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import TariffPlan, Simcard

from .forms import *

from CRUD_System.tasks import send_client_creation_message

# Create your views here.


@login_required(login_url='login-request')
def main(request):

    if request.method == "POST":

        # Добавление записи пользователя
        if request.POST.get("action") == "create":
            current_tariff = TariffPlan.objects.filter(pk=request.POST.get("add-record-ServiceType"))

            client_name = request.POST.get("add-record-CustomerName")
            client_phone = request.POST.get('add-record-Phone')

            SimcardRecord = Simcard(IMEI=request.POST.get('add-record-IMEI'),
                                    PhoneNumber=client_phone,
                                    ClientName=client_name,
                                    RegistrationDate=request.POST.get("add-record-RegDate"),
                                    TariffPlan=current_tariff[0])

            SimcardRecord.save()

            # Отправка сообщения о создании нового пользователя
            task_result = send_client_creation_message.delay(client_name, client_phone)

            print(f"Задача успешно отправлена с id: {task_result.id}")

            print("Запись клиента успешно создана...")

            return redirect('/')


        # Обновление записи пользователя
        if request.POST.get("action") == "update":
            
            current_tariff = TariffPlan.objects.filter(pk=request.POST.get("update-record-ServiceType-pk"))

            current_simcard_record = Simcard.objects.get(id=request.POST.get('update-record-simcard-pk'))

            current_simcard_record.IMEI = request.POST.get('update-record-IMEI')
            current_simcard_record.PhoneNumber = request.POST.get('update-record-Phone')
            current_simcard_record.ClientName = request.POST.get('update-record-CustomerName')
            current_simcard_record.RegistrationDate = request.POST.get('update-record-RegDate')
            current_simcard_record.TariffPlan = current_tariff[0]

            current_simcard_record.save()

            print("Запись клиента успешно обновлена...")

            return redirect('/')


        # Удаление записи пользователя
        if request.POST.get("action") == "delete":
            deleted_record_id = request.POST.get("deleted-record-pk")

            if not deleted_record_id:
                return HttpResponseBadRequest(
                    "ID клиента не был передан на удаление"
                )

            deleted_count, _ = Simcard.objects.filter(
                pk=deleted_record_id
            ).delete()

            if deleted_count == 0:
                return HttpResponseBadRequest(
                    "Запись с указанным ID не найдена"
                )
    
            print("Запись клиента успешно удалена...")

            return redirect('/')
            

    context = {"Simcards": Simcard.objects.all(),
               "TariffPlan": TariffPlan.objects.all()}

    return render(request, "CRUD_System/Simcard_CRUD.html", context=context)


def login_request(request):

    if request.method == "POST":
        form = CRUDSystemLoginForm(request.POST)
        if form.is_valid():
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

