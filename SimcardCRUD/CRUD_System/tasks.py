from celery import shared_task

from celery.utils.log import get_task_logger

from django.conf import settings
from django.core.mail import send_mail

# Создаем специальный безопасный логгер
logger = get_task_logger(__name__)

@shared_task(name="send_client_creation_message")
def send_client_creation_message(client_name, client_phone):

    message = (
        f"Клиент '{client_name}' "
        f"с телефоном '{client_phone}' "
        f"был успешно создан."
    )

    # logger.info гарантированно напечатает строку в консоли Celery
    logger.info(message) 

    send_mail(
        subject="Регистрация нового клиента в системе",
        message=message,
        from_email=None,
        recipient_list=["iveschkin@yandex.ru"],
        fail_silently=False,
    )

    return message


@shared_task(name="every_5_minutes_task")
def every_5_minutes_task():

    message = "Данная задача выполняется каждые 5 минут!"

    # logger.info гарантированно напечатает строку в консоли Celery
    logger.info(message) 


@shared_task(name="task_to_be_executed_everyday_at_17_45")
def task_to_be_executed_everyday_at_17_45():

    message = "Данная задача выполняется каждые день в 17:45!"

    # logger.info гарантированно напечатает строку в консоли Celery
    logger.info(message) 