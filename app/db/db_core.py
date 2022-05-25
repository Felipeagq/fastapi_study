from abc import ABC, abstractmethod
from typing import Optional, TypeVar

T = TypeVar("T")

class Database(ABC):

    # @abstractmethod
    # def open(self)->None:
    #     pass

    @abstractmethod
    def create(**kwargs):
        pass

    @abstractmethod
    def read(self,**kwargs):
        pass

    # @abstractmethod
    # def update(self,**kwargs):
    #     pass

    # @abstractmethod
    # def delete(self,**kwargs):
    #     pass

    # @abstractmethod
    # def close(self)->None:
    #     pass
