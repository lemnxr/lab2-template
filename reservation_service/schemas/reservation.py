from pydantic import BaseModel, constr, conint
from uuid import UUID
from datetime import datetime as dt

from enums.status import ReservationStatus


def convert_datetime(datetime: dt) -> str:
    return datetime.strftime('%Y-%m-%d') 

class ReservationBase(BaseModel):
    username: constr(max_length=80)
    hotel_id: int | None
    status: ReservationStatus
    start_date: dt
    end_date: dt

class ReservationRequest(ReservationBase):
    hotel_id: int | None = None

class Reservation(ReservationBase):
    id: int
    reservation_uid: UUID
    payment_uid: UUID

class ReservationUpdate(BaseModel):
    status: ReservationStatus | None = None
    start_date: dt | None = None
    end_date: dt | None = None
    