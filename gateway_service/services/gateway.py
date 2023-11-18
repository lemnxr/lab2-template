from uuid import UUID
from datetime import datetime

from cruds.interfaces.reservation import IReservationCRUD
from cruds.interfaces.payment import IPaymentCRUD
from cruds.interfaces.loyalty import ILoyaltyCRUD
from exceptions.exceptions import NotFoundException
from enums.status import ReservationStatus, PaymentStatus, LoyaltyStatus
from schemas.user import UserInfoResponse
from schemas.reservation import *
from schemas.payment import PaymentInfo
from schemas.loyalty import LoyaltyInfoResponse, CreateLoyaltyRequest


class GatewayService():
    def __init__(self,
                 reservationCRUD: type[IReservationCRUD],
                 paymentCRUD: type[IPaymentCRUD],
                 loyaltyCRUD: type[ILoyaltyCRUD]
                 ):
        self._reservationCRUD = reservationCRUD()
        self._paymentCRUD = paymentCRUD()
        self._loyaltyCRUD = loyaltyCRUD()

    async def get_all_hotels(self, page: int, size: int):
        hotels_list = await self._reservationCRUD.get_all_hotels(page=page, size=size)
        hotels_num = await self._reservationCRUD.get_hotels_num()
        hotels = []
        
        for hotel_dict in hotels_list:
            hotels.append(
                HotelResponse(
                    hotel_uid=hotel_dict["hotel_uid"],
                    name=hotel_dict["name"],
                    country=hotel_dict["country"],
                    city=hotel_dict["city"],
                    address=hotel_dict["address"],
                    stars=hotel_dict["stars"],
                    price=hotel_dict["price"]
                )
            )
        
        return PaginationResponse(
            page=page,
            pageSize=size,
            totalElements=hotels_num,
            items=hotels
        )
    
    async def __get_hotel_by_id(self, hotel_id: int):
        if hotel_id:
            hotel_dict = await self._reservationCRUD.get_hotel_by_id(hotel_id)
            print(hotel_dict)
        else:
            hotel_dict = None
        return hotel_dict
    
    async def __get_payment_by_uid(self, payment_uid: int):
        if payment_uid:
            payment_dict = await self._paymentCRUD.get_payment_by_uid(payment_uid)
            print(payment_dict)
        else:
            payment_dict = None
        return payment_dict
    
    async def _get_user_reservations_hotels(self, user_name: str):
        reservations_list = await self._reservationCRUD.get_all_reservations(user_name=user_name)
       
        reservations = []

        for reservation_dict in reservations_list:
            hotel_dict = await self.__get_hotel_by_id(reservation_dict["hotel_id"])
            payment_dict = await self.__get_payment_by_uid(reservation_dict["payment_uid"])

            print(hotel_dict)
            print(type(hotel_dict))
            print(hotel_dict["hotel_uid"])

            print(reservation_dict["start_date"])
            print(type(reservation_dict["start_date"]))
    
            hotel_info = HotelInfo(
                hotel_uid=hotel_dict["hotel_uid"],
                name=hotel_dict["name"],
                fullAddress=hotel_dict["country"]+", "+hotel_dict["city"]+", "+hotel_dict["address"],
                stars=hotel_dict["stars"]
                )
            
            payment_info = PaymentInfo(
                status=payment_dict["status"],
                price=payment_dict["price"]
                )

            reservations.append(
                ReservationResponse(
                    reservation_uid=reservation_dict["reservation_uid"],
                    hotel=hotel_info,
                    start_date=reservation_dict["start_date"],
                    end_date=reservation_dict["end_date"],
                    status=reservation_dict["status"],
                    payment=payment_info
                )
            )
        print(reservations)
        return reservations
    
    # async def get_new_loyalty(self, user_name: str):
    #     loyalty_id = await self._loyaltyCRUD.create_new_loyalty(
    #         LoyaltyCreate(
    #             username = user_name,
    #             status = "BRONZE",
    #             discount = 0,
    #             reservation_count = 0
    #         )
    #     )

    async def __get_loyalty_by_username(self, user_name):
        if user_name:
            loyalty_dict = await self._loyaltyCRUD.get_loyalty_by_username(user_name)
            print(loyalty_dict)
        else:
            loyalty_dict = None
            print(loyalty_dict)
            print("NONONONO")
        return loyalty_dict
    
    async def _get_user_loyalty(self, user_name: str):
        loyalty_dict = await self.__get_loyalty_by_username(user_name)

        if loyalty_dict == []:
            loyalty_dict.append(await self._loyaltyCRUD.get_new_loyalty(
                CreateLoyaltyRequest(
                    username=user_name,
                    status="BRONZE",
                    discount=0,
                    reservation_count=0
                )
            )
        )
        #else:
        #    loyalty_dict = loyalty_dict[0]
        print(loyalty_dict)
        loyalty = LoyaltyInfoResponse(
                        status=loyalty_dict[0]["status"],
                        discount=loyalty_dict[0]["discount"],
                        reservation_count=loyalty_dict[0]["reservation_count"]
                        )
        
        return loyalty
        
        # loyalty_list = await self._loyaltyCRUD.get_all_loyalty(user_name = user_name)

        # if len(loyalty_list):
        #     loyalty_dict = loyalty_list[0]
        # else:
        #     loyalty_dict = await self.get_new_loyalty(user_name)

        # return loyalty_dict
         
    
    async def get_user_info(self, user_name: str):
        reservations = await self._get_user_reservations_hotels(user_name)
        loyalty = await self._get_user_loyalty(user_name)

        return UserInfoResponse(
            reservations=reservations,
            loyalty=loyalty
        )

    async def get_user_reservations(self, user_name: str):
        reservations = await self._get_user_reservations_hotels(user_name)
        return reservations
    