from pydantic import BaseModel, constr, conint, validator
from uuid import UUID
from datetime import datetime, date

from enums.status import ReservationStatus


class ReservationBase(BaseModel):
    username: constr(max_length=80)
    hotel_id: int | None
    status: ReservationStatus
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

class ReservationRequest(ReservationBase):
    hotel_id: int | None = None

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

class Reservation(ReservationBase):
    id: int
    reservation_uid: UUID
    payment_uid: UUID

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

class ReservationUpdate(BaseModel):
    status: ReservationStatus | None = None
    start_date: date | None = None
    end_date: date | None = None

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
    