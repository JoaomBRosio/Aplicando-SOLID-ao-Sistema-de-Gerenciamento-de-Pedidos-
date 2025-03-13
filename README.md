# Sistema de Gerenciamento de Pedidos

Este projeto é um sistema de gerenciamento de pedidos que aplica os princípios SOLID para garantir um código mais modular, flexível e de fácil manutenção.


## Descrição dos Arquivos

- **CalculadoraFrete.py**: Define a interface `CalculadoraFrete` com o método abstrato `calcular_frete`.
- **CalculadoraFretePadrao.py**: Implementa a interface `CalculadoraFrete` com uma taxa de frete fixa.
- **CalculadoraTaxa.py**: Define a interface `CalculadoraTaxa` com o método abstrato `calcular_taxa`.
- **CalculadoraTaxaPadrao.py**: Implementa a interface `CalculadoraTaxa` com uma taxa de 10%.
- **IPedido.py**: Define a interface `IPedido` com o método abstrato `calcular_total`.
- **Pedido.py**: Define a classe abstrata `Pedido` que implementa a interface `IPedido`.
- **PedidoDigital.py**: Implementa a classe `Pedido` para pedidos digitais.
- **PedidoFisico.py**: Implementa a classe `Pedido` para pedidos físicos.
- **Main.py**: Script principal que cria instâncias de pedidos físicos e digitais e calcula seus totais.

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Navegue até o diretório `src`.
3. Execute o script `Main.py`:
    ```sh
    python Main.py
    ```

## Princípios SOLID Aplicados

1. **Single Responsibility Principle (SRP)**: Cada classe tem uma única responsabilidade. Por exemplo, `CalculadoraFretePadrao` é responsável apenas pelo cálculo do frete, enquanto `PedidoFisico` é responsável por representar um pedido físico.

2. **Open/Closed Principle (OCP)**: As classes estão abertas para extensão, mas fechadas para modificação. Por exemplo, podemos criar novas classes de calculadoras de frete ou taxa sem modificar as existentes.

3. **Liskov Substitution Principle (LSP)**: As subclasses podem ser usadas no lugar das classes base sem alterar o comportamento esperado. Por exemplo, `PedidoFisico` e `PedidoDigital` podem ser usadas onde `Pedido` é esperado.

4. **Interface Segregation Principle (ISP)**: As interfaces são específicas e não forçam a implementação de métodos desnecessários. Por exemplo, `CalculadoraFrete` e `CalculadoraTaxa` são interfaces separadas.

5. **Dependency Inversion Principle (DIP)**: As classes dependem de abstrações e não de implementações concretas. Por exemplo, `Pedido` depende de `CalculadoraTaxa` e `CalculadoraFrete`, que são abstrações.
