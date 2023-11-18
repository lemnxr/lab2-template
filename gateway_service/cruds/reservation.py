import requests
from requests import Response

from cruds.interfaces.reservation import IReservationCRUD
from cruds.base import BaseCRUD


class ReservationCRUD(IReservationCRUD, BaseCRUD):
    def __init__(self):
        self.http_path = f'http://reservation_service:8070/api/v1/'

    async def get_all_hotels(
            self,
            page: int = 1,
            size: int = 100,
        ):
        response: Response = requests.get(
            url=f'{self.http_path}hotels/?page={page}&size={size}'
        )
        return response.json()
        
    async def get_hotels_num(
            self
    ):
        response: Response = requests.get(
            url=f'{self.http_path}hotels/'
        )
        return len(response.json())
    
    async def get_hotel_by_id(
            self,
            hotel_id
    ):
        response: Response = requests.get(
            url=f'{self.http_path}hotels/{hotel_id}'
        )
        return response.json()
    
    async def get_all_reservations(
            self,
            user_name: str
    ):
        response: Response = requests.get(
            url=f'{self.http_path}reservations/?username={user_name}'
        )
        return response.json()
        