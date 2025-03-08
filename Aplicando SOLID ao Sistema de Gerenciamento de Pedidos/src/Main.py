from PedidoFisico import PedidoFisico
from PedidoDigital import PedidoDigital
from CalculadoraFretePadrao import CalculadoraFretePadrao
from CalculadoraTaxaPadrao import CalculadoraTaxaPadrao

if __name__ == "__main__":
    calculadora_taxa = CalculadoraTaxaPadrao()
    calculadora_frete = CalculadoraFretePadrao()

    id_fisico = input("Digite o ID do Pedido Físico: ")
    cliente_fisico = input("Digite o nome do Cliente do Pedido Físico: ")
    valor_fisico = float(input("Digite o valor do Pedido Físico: "))

    id_digital = input("Digite o ID do Pedido Digital: ")
    cliente_digital = input("Digite o nome do Cliente do Pedido Digital: ")
    valor_digital = float(input("Digite o valor do Pedido Digital: "))

    pedido_fisico = PedidoFisico(id_fisico, cliente_fisico, valor_fisico, calculadora_taxa, calculadora_frete)
    pedido_digital = PedidoDigital(id_digital, cliente_digital, valor_digital, calculadora_taxa)

    print(f"Total Pedido Físico: {pedido_fisico.calcular_total()}")
    print(f"Total Pedido Digital: {pedido_digital.calcular_total()}")