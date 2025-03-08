from abc import ABC, abstractmethod

class CalculadoraFrete(ABC):
    @abstractmethod
    def calcular_frete(self) -> float:
        pass
