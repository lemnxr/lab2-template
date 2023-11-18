from abc import ABC, abstractmethod


class IPaymentCRUD(ABC):
    @abstractmethod
    async def get_all_payments(
        self,
        page: int = 1,
        size: int = 100
    ) -> list[dict]:
        pass
    
    @abstractmethod
    async def get_payment_by_uid(
        self,
    ) ->list[dict]:
        pass
