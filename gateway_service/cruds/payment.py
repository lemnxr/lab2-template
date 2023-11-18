import requests
from requests import Response

from cruds.interfaces.payment import IPaymentCRUD
from cruds.base import BaseCRUD


class PaymentCRUD(IPaymentCRUD, BaseCRUD):
    def __init__(self):
        self.http_path = f'http://payment_service:8060/api/v1/'

    async def get_all_payments(
            self,
            page: int = 1,
            size: int = 100,
        ):
        response: Response = requests.get(
            url=f'{self.http_path}payments/?page={page}&size={size}'
        )
        return response.json()
    
    async def get_payment_by_uid(
            self,
            payment_uid
    ):
        response: Response = requests.get(
            url=f'{self.http_path}payments/{payment_uid}'
        )
        return response.json()
        