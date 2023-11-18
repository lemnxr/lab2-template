import requests
import json
from requests import Response

from cruds.interfaces.loyalty import ILoyaltyCRUD
from cruds.base import BaseCRUD
from schemas.loyalty import CreateLoyaltyRequest


class LoyaltyCRUD(ILoyaltyCRUD, BaseCRUD):
    def __init__(self):
        self.http_path = f'http://loyalty_service:8050/api/v1/'

    async def get_all_loyalties(
            self,
            page: int = 1,
            size: int = 100,
        ):
        response: Response = requests.get(
            url=f'{self.http_path}loyalties/?page={page}&size={size}'
        )
        return response.json()
        
    async def get_loyalty_by_username(
            self,
            user_name
    ):
        response: Response = requests.get(
            url=f'{self.http_path}loyalties/?username={user_name}'
        )
        return response.json()
    
    async def get_new_loyalty(
            self,
            loyalty: CreateLoyaltyRequest
    ):
        loyalty_data = {"username": f"{loyalty.username}", "status": f"{loyalty.status}", "discount": loyalty.discount, "reservation_count": loyalty.reservation_count}
        loyalty_data_json = json.dumps(loyalty_data)
        #print(loyalty_data)
        #print(type(loyalty_data))
        requests.post(url=f'{self.http_path}loyalties/', data=loyalty_data_json)
        return loyalty_data
    