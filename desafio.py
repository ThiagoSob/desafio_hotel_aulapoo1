class Funcionarios:
    def __init__ (self , nome , funcao , salario):
        self.nome = nome
        self.funcao = funcao
        self.salario = salario

f1 = Funcionarios(nome='Thiago' , funcao='CO' , salario=17000.00)
f2 = Funcionarios(nome='Ursula' , funcao='Diretor' , salario=15000.00)
f3 = Funcionarios(nome='Matheus' , funcao='Coordenador' , salario=12000.00)
f4 = Funcionarios(nome='Paulo' , funcao='Recepção' , salario=5000.00)
f5 = Funcionarios(nome='Carla' , funcao='Arrumadeira' , salario=3500.00)

class Item:
    def __init__ (self , nome , preco_unitario , quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
    
class Fatura:
    def __init__ (self , itens : list):
        self.itens = itens
    
    def gerar_fatura(self):
        valor = 0
        
        for compra in self.itens:
            custo_compra = compra.quantidade * compra.preco_unitario
            
            print(f' - {compra.nome}: {custo_compra:.2f}')
            
            
            valor += custo_compra
        
        print('')
            
        return valor

class Hotel:
    def __init__ (self , reserva : bool , quarto : str ):
        self.reserva = reserva
        self.quarto = quarto
    
    def status_quarto(self , x):
        if self.reserva == True:
            print(f'{x} Reservado!')
        else:
            print(f'{x} Livre!')
    

class Empresa_Hotel:
    def __init__ (self , nome):
        self.nome = nome
        self.lista_funcionarios = []
    
    def listar(self):
        if len(self.lista_funcionarios) == 0:
            print('Não existe funcionário cadastrado!')
        else:    
            print('')
            print('Lista de Funcionários:')
            for funcionario in self.lista_funcionarios:
                print(funcionario)
    
    def adicionar(self , x):
        self.lista_funcionarios.append(x)
        print('')
        print(f'O funcionário {x} foi contratado!')
        print('')
    
    def remover(self , y):
        self.lista_funcionarios.remove(y)
        print('')
        print(f'O funcionário {y} foi demitido.')
        print('')
    
nome_hotel = Empresa_Hotel(nome='IPS')

print('')
print('Quadro de Funcionários do Hotel:')
print('')

nome_hotel.listar()

print('')

nome_hotel.adicionar(f1.nome)
nome_hotel.adicionar(f2.nome)
nome_hotel.adicionar(f3.nome)
nome_hotel.adicionar(f4.nome)
nome_hotel.adicionar(f5.nome)

print('')

nome_hotel.listar()

print('')

q1 = Hotel(reserva=True , quarto='Quarto 401')
q2 = Hotel(reserva=False , quarto='Quarto 305')
q3 = Hotel(reserva=True , quarto='Quarto 207')
q4 = Hotel(reserva=False , quarto='Quarto 101')
q5 = Hotel(reserva=True , quarto='Quarto 509')

print('Situação dos Quartos:')
print('')

q1.status_quarto(q1.quarto)
q2.status_quarto(q2.quarto)
q3.status_quarto(q3.quarto)
q4.status_quarto(q4.quarto)
q5.status_quarto(q5.quarto)



print('')

item1q1 = Item(nome=q1.quarto, quantidade= 2, preco_unitario= 250)

item2q1 = Item(nome= 'Chocolate', quantidade=3 , preco_unitario=11.90)

compraq1 = [item1q1 , item2q1]

faturaq1 = Fatura(itens=compraq1)

print('')
print(f'A fatura do {q1.quarto}: ')
print('')

print(f'A fatura ficou: R${faturaq1.gerar_fatura():.2f}')
