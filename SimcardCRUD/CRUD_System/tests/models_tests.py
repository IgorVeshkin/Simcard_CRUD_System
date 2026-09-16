import pytest

from CRUD_System.models import Simcard, TariffPlan

from datetime import date
from django.utils import timezone

import random


@pytest.mark.django_db
def test_create_tarrif():

    tariff = TariffPlan.objects.create(
        Title="Тестовый тарифный план",
        Minutes="100",
        SMS="100",
        Gigabytes="100",
        Price=100
    )

    assert str(tariff) == tariff.Title == "Тестовый тарифный план"

@pytest.mark.django_db
def test_create_simcard():

    tariff = TariffPlan.objects.create(
        Title="Тестовый тарифный план",
        Minutes="100",
        SMS="100",
        Gigabytes="100",
        Price=100
    )

    simcard = Simcard.objects.create(
        IMEI="860870370916418",
        PhoneNumber="+70000000000",
        ClientName="Тестовое Имя Пользователя",
        RegistrationDate=timezone.localdate(),
        TariffPlan = tariff

    )

    assert simcard.IMEI == "860870370916418"
    assert isinstance(simcard.RegistrationDate, date)

    assert tariff == simcard.TariffPlan