from abc import ABC, abstractmethod

class IPedido(ABC):
    @abstractmethod
    def calcular_total(self) -> float:
        pass
