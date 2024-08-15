##  Gerenciamento De Hotel
# Sistema de Gerenciamento de Hotel

![Hotel Management System](https://img.shields.io/badge/Project-Hotel%20Management%20System-brightgreen)

Este projeto é um sistema de gerenciamento para um hotel, que inclui funcionalidades para administrar funcionários, verificar o status dos quartos e gerar faturas para itens consumidos. O sistema é desenvolvido em Python e é dividido em várias classes para representar diferentes aspectos do hotel.

## Funcionalidades

- **Gerenciamento de Funcionários**: Adicionar, listar e remover funcionários do hotel.
- **Status dos Quartos**: Verificar se os quartos estão reservados ou livres.
- **Geração de Faturas**: Calcular e exibir faturas para itens consumidos em um quarto.


## Como Usar

1. **Criação de Funcionários**:
   - Instancie objetos da classe `Funcionarios` com nome, função e salário.

2. **Gerenciamento de Funcionários**:
   - Adicione funcionários à lista usando o método `adicionar`.
   - Liste todos os funcionários com o método `listar`.
   - Remova funcionários da lista com o método `remover`.

3. **Gerenciamento de Quartos**:
   - Instancie objetos da classe `Hotel` para representar quartos, com informações sobre reserva.
   - Verifique o status dos quartos com o método `status_quarto`.

4. **Geração de Faturas**:
   - Crie objetos da classe `Item` para itens consumidos.
   - Adicione esses itens a uma lista e crie uma fatura com a classe `Fatura`.
   - Use o método `gerar_fatura` para calcular e exibir o valor total da fatura.

## Exemplo de Uso

```python
# Criando Funcionários
f1 = Funcionarios(nome='Thiago', funcao='CO', salario=17000.00)
f2 = Funcionarios(nome='Ursula', funcao='Diretor', salario=15000.00)

# Gerenciando Funcionários
nome_hotel = Empresa_Hotel(nome='IPS')
nome_hotel.adicionar(f1)
nome_hotel.adicionar(f2)
nome_hotel.listar()

# Gerenciando Quartos
q1 = Hotel(reserva=True, quarto='Quarto 401')
q1.status_quarto()

# Gerando Faturas
item1 = Item(nome='Quarto 401', quantidade=2, preco_unitario=250)
item2 = Item(nome='Chocolate', quantidade=3, preco_unitario=11.90)
fatura = Fatura(itens=[item1, item2])
print(f'A fatura ficou: R${fatura.gerar_fatura():.2f}')
