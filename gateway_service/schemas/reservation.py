from pydantic import BaseModel, conint, constr
from datetime import datetime as dt
from uuid import UUID

from enums.status import ReservationStatus
from schemas.payment import PaymentInfo


def convert_datetime(datetime: dt) -> str:
    return datetime.strftime('%Y-%m-%d') 

class HotelResponse(BaseModel):
    hotel_uid: UUID
    name: constr(max_length=255)
    country: constr(max_length=80)
    city: constr(max_length=80)
    address: constr(max_length=255)
    stars: conint(ge=1) | None = None
    price: conint(ge=1)

class PaginationResponse(BaseModel):
    page: conint(ge=1)
    pageSize: conint(ge=1)
    totalElements: conint(ge=0)
    items: list[HotelResponse]

class HotelInfo(BaseModel):
    hotel_uid: UUID
    name: constr(max_length=255)
    fullAddress: constr(max_length=255)
    stars: conint(ge=1) | None = None

class ReservationResponse(BaseModel):
    reservation_uid: UUID
    hotel: HotelInfo
    start_date: dt
    end_date: dt
    status: ReservationStatus
    payment: PaymentInfo

    class Config:
        json_encoders = {dt: convert_datetime}

class CreateReservationRequest(BaseModel):
    hotel_uid: UUID
    start_date: dt
    end_date: dt

    class Config:
        json_encoders = {dt: convert_datetime}

class CreateReservationResponse(BaseModel):
    reservation_uid: UUID
    hotel_uid: UUID
    start_date: dt
    end_date: dt
    discount: int
    status: ReservationStatus
    payment: PaymentInfo
    
    class Config:
        json_encoders = {dt: convert_datetime}
