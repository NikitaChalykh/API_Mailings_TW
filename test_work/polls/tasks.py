import logging
import os
import time
import sys
from datetime import datetime

import requests
from dotenv import load_dotenv

from mailings.models import Contact, Mailing, Message

load_dotenv()

logging.basicConfig(
    format='%(asctime)s %(name)s %(levelname)s  %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)],
    level=logging.ERROR
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

RETRY_TIME = 10
TIME_FORMAT = "%Y-%m-%d - %H:%M:%S"
SENDING_API_TOKEN = os.getenv('SENDING_API_TOKEN')


class MissingValueException(Exception):
    """Создаем свое исключения при отсутствии переменных окружения."""


class GetAPIException(Exception):
    """Создаем свое исключение при сбое запроса к API отправки сообщений."""


def send_api_message(message_id, contact, message):
    """Отправляем сообщение через внешнее API"""
    headers = {'Authorization': f'Bearer {SENDING_API_TOKEN}'}
    json = {
        "phone": contact,
        "text": message
    }
    try:
        response = requests.post(
            f'https://probe.fbrq.cloud/v1/send/{message_id}'.format(
                message_id=message_id
            ),
            headers=headers,
            json=json
        )
        logger.info('Сообщение отправлено через венешний API')
        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as error:
        logger.error(f'Сбой при отправке сообщения: {error}')
        return False


def start_mailings():
    """Основной код обработки рассылок."""
    logger.debug('-----------------')
    message_id = [1]
    finished_mailing_id = []
    if SENDING_API_TOKEN is None:
        logger.critical('Отсутствуют переменные окружения!')
        raise MissingValueException('Отсутствуют переменные окружения!')
    while True:
        try:
            logger.debug('Начало новой иттерации')
            mailings = Mailing.objects.all()
            for mailing in mailings:
                current_datetime = datetime.now()
                if (
                    datetime.strptime(
                        mailing['start_send_time'], TIME_FORMAT
                    ) <= current_datetime
                    and datetime.strptime(
                        mailing['end_send_time'], TIME_FORMAT
                    ) >= current_datetime
                    and mailing['id'] not in finished_mailing_id
                ):
                    mailing_id = mailing['id']
                    tag = mailing['tag']
                    code = mailing['code']
                    text = mailing['text']
                    contacts = Contact.objects.filter(
                        tag=tag
                    ).filter(
                        code=code
                    )
                    for contact in contacts:
                        current_datetime = datetime.now()
                        contact_id = contact['id']
                        if (
                            current_datetime <= datetime.strptime(
                                mailing['end_send_time'], TIME_FORMAT
                            ) and send_api_message(
                                message_id[0],
                                contact,
                                text
                            )
                        ):
                            Message.objects.create(
                                status='S',
                                mailing=mailing_id,
                                contact=contact_id
                            )
                        else:
                            Message.objects.create(
                                status='N',
                                mailing=mailing_id,
                                contact=contact_id
                            )
                        message_id[0] += 1
                    finished_mailing_id.append(mailing_id)
            logger.debug('Конец иттерации')
            logger.debug('-----------------')
            time.sleep(RETRY_TIME)
        except Exception as error:
            logger.error(f'Сбой в работе программы: {error}')
            logger.debug('-----------------')
            time.sleep(RETRY_TIME)
