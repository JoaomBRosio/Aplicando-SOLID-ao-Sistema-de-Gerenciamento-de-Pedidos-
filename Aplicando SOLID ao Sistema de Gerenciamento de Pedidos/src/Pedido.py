from IPedido import IPedido
from CalculadoraTaxa import CalculadoraTaxa

class Pedido(IPedido):
    def __init__(self, id: str, cliente: str, valor_base: float, calculadora_taxa: CalculadoraTaxa):
        self.id = id
        self.cliente = cliente
        self.valor_base = valor_base
        self.calculadora_taxa = calculadora_taxa

    def calcular_total(self) -> float:
        raise NotImplementedError("Subclasses devem implementar este método.")
