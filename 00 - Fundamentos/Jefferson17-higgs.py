# sistema bancario

conta_bancaria= float(3000)
limite_diario_saques= 0
lista_deposistos= []
lista_saques= []

MENU= 'Menu'
EXTRATO= 'Extrato'

while True:
    
    print('')
    print(MENU.center(24, '-'))
    print('''\n
          
    1. Deposito
    2. Saque
    3. Extrato
    4. Sair
          
          ''')
    print('-'*24,'\n')

    escolha_usuario= int(input('Selecione a opção que deseja: '))

    if escolha_usuario == 1:
        
        print(f'\nSaldo em conta: {conta_bancaria:.2f}')
        deposito_usuario= int(input('Digite o valor de deposito: '))
        
        permitir_deposito= conta_bancaria+deposito_usuario  if deposito_usuario > 0 else 'Valor invalido, selecione putro valor.'
        conta_bancaria= permitir_deposito
        lista_deposistos.append(deposito_usuario)    
        print(f'Saldo atual: {conta_bancaria:.2f}' if permitir_deposito == type(1) else permitir_deposito)
    
    elif escolha_usuario == 2:
        
            saque_usuario= int(input('\nDigite o valor de saque: '))
            
            if saque_usuario <= 500:
                
                limite_diario_saques+= 1
                
                if limite_diario_saques <= 3:
                
                    permitir_saque= conta_bancaria-saque_usuario if conta_bancaria > 0 else 'Não a saudo suficiente'
                    conta_bancaria= permitir_saque
                    lista_saques.append(saque_usuario)
                    print(f'Saldo atual: {conta_bancaria:.2f}' if permitir_saque == type(1) else permitir_saque)
                
                else:
                    
                    print('Limite diario de saques excedido.')
                                
            else:
                
                print('Limite de R$ 500.00 excedido.')
    
            
    elif escolha_usuario == 3:
        
        print('')
        print(EXTRATO.center(27, '-'))
        
        for deposito, saque in zip(lista_deposistos, lista_saques):
            

            print(f'''\n 
                
                Depositos: {deposito:.f}
                Saques: {saque:.2f}
                
                
                
                ''')     
                
        else:
            
            print('Não foram realizadas movimentações.')
              
              
        print(f'Saldo atual da conta: {conta_bancaria:.2f}\n')
        print('-'*24,'\n')
        
    elif escolha_usuario == 4:
        
        print('\nOperação encerrada, obrigado.')
        break
    
    else:
        
        print('\nValor invalido, digite um valor valido.')
        