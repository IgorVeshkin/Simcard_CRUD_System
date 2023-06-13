from django import template
from CRUD_System.models import *

register = template.Library()


@register.simple_tag(name="FetchRecordForUpdateForm")
def FetchRecordForUpdateForm(record_id):
    return Simcard.objects.get(id=record_id)


@register.filter(name="PhoneNumberForm")
def PhoneNumberForm(phone_number):
    return phone_number[0:2] + " " + "(" + phone_number[2:5] + ")" + " " + phone_number[5:8] + " " + phone_number[8:10] + "-" + phone_number[10:12]