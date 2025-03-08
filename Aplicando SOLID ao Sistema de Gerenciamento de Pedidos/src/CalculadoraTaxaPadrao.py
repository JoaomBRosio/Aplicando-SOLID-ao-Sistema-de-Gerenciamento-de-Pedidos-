from CalculadoraTaxa import CalculadoraTaxa

class CalculadoraTaxaPadrao(CalculadoraTaxa):
    def calcular_taxa(self, valor_base: float) -> float:
        return valor_base * 0.1  # 10% de taxa
