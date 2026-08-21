from celery import shared_task

from celery.utils.log import get_task_logger

# Создаем специальный безопасный логгер
logger = get_task_logger(__name__)

@shared_task(name="send_client_creation_message")
def send_client_creation_message(clientName, clientPhone):

    message =  f"Клиент \'{clientName}\' с телефоном \'{clientPhone}\' был успешно создан"

    # logger.info гарантированно напечатает строку в консоли Celery
    logger.info(message) 

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