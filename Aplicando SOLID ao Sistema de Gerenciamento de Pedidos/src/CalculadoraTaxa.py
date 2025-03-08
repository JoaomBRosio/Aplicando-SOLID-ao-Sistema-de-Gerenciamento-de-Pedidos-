from abc import ABC, abstractmethod

class CalculadoraTaxa(ABC):
    @abstractmethod
    def calcular_taxa(self, valor_base: float) -> float:
        pass
