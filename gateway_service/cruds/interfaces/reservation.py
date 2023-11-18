from abc import ABC, abstractmethod


class IReservationCRUD(ABC):
    @abstractmethod
    async def get_all_hotels(
        self,
        page: int = 1,
        size: int = 100
    ) -> list[dict]:
        pass
    
    @abstractmethod
    async def get_hotels_num(
        self
    ) -> int:
        pass

    @abstractmethod
    async def get_hotel_by_id(
        self,
    ) -> list[dict]:
        pass

    @abstractmethod
    async def get_all_reservations(
        self
    ) -> list[dict]:
        pass
