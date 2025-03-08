from Pedido import Pedido
from CalculadoraFrete import CalculadoraFrete

class PedidoFisico(Pedido):
    def __init__(self, id: str, cliente: str, valor_base: float, calculadora_taxa, calculadora_frete: CalculadoraFrete):
        super().__init__(id, cliente, valor_base, calculadora_taxa)
        self.calculadora_frete = calculadora_frete

    def calcular_total(self) -> float:
        return self.valor_base + self.calculadora_frete.calcular_frete() + self.calculadora_taxa.calcular_taxa(self.valor_base)
