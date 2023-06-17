from abc import ABC, abstractmethod


class Service(ABC):
    @staticmethod
    @abstractmethod
    async def parse_items(items: list) -> list:
        pass
