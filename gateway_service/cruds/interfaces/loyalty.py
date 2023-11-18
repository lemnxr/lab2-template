from abc import ABC, abstractmethod


class ILoyaltyCRUD(ABC):
    @abstractmethod
    async def get_all_loyalties(
        self,
        page: int = 1,
        size: int = 100
    ) -> list[dict]:
        pass
    
    @abstractmethod
    async def get_loyalty_by_username(
        self,
    ) ->list[dict]:
        pass

    @abstractmethod
    async def get_new_loyalty(
        self,
    ) ->list[dict]:
        pass
