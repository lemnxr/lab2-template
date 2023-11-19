from pydantic import BaseModel, conint, constr, validator
from datetime import datetime, date
from uuid import UUID

from enums.status import ReservationStatus
from schemas.payment import PaymentInfo


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
    # class Config:
    #     json_encoders = {dt: convert_datetime}

    reservation_uid: UUID
    hotel: HotelInfo
    start_date: date
    end_date: date
    status: ReservationStatus
    payment: PaymentInfo

    @validator("start_date", pre=True)
    def parse_start_date(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()

    @validator("end_date", pre=True)
    def parse_end_date(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()


class CreateReservationRequest(BaseModel):
    # class Config:
    #     json_encoders = {dt: convert_datetime}

    hotel_uid: UUID
    start_date: date
    end_date: date

    @validator("start_date", pre=True)
    def parse_start_date(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()

    @validator("end_date", pre=True)
    def parse_end_date(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()

class CreateReservationResponse(BaseModel):
    # class Config:
    #     json_encoders = {dt: convert_datetime}

    reservation_uid: UUID
    hotel_uid: UUID
    start_date: date
    end_date: date
    discount: int
    status: ReservationStatus
    payment: PaymentInfo

    @validator("start_date", pre=True)
    def parse_start_date(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()

    @validator("end_date", pre=True)
    def parse_end_date(cls, value):
        return datetime.strptime(
            value,
            "%Y-%m-%d"
        ).date()
