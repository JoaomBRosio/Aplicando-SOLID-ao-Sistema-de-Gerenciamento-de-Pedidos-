from Pedido import Pedido

class PedidoDigital(Pedido):
    def calcular_total(self) -> float:
        return self.valor_base + self.calculadora_taxa.calcular_taxa(self.valor_base)
