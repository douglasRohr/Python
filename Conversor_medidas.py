'''CONVERSOR DE MEDIDAS'''

# CÓDIGO FUNCIONANDO OK

# CÓDIGO RETORNA AO MENU CORRETAMENTE QUANDO SÃO INSERIDOS CARACTERES INVÁLIDOS

print('Bem-vindo ao conversor de medidas!')
while True:
    try: # USADO PARA TRATAMENTO DE ERROS
        menu = int(input('''
O que deseja converter?
                                       
[1] Metros em centímetros
[2] Centímetros em metros
[3] Sair
                                         
Digite sua opção: '''))
    
        if menu == 3:
            print('Até a próxima!')
            exit()
        if menu >= 1 or menu <= 2:
            match menu: # AJUSTAR RETORNO OPCIONAL AO MENU APÓS A CONVERSÃO
                case 1:
                    calc_ctms = float(input('Digite o valor em metro(s) a converter: '))
                    print(f'Convertendo {calc_ctms} metro(s) para centímetro(s) obtemos: {calc_ctms * 100} centímetros.\n')
                case 2:
                    calc_mts = float(input('Valor em centímetro(s) a converter: '))
                    print(f'Convertendo {calc_mts} centímetro(s) para metro(s) obtemos: {calc_mts / 100} metros.\n')
    except ValueError:
        print('\nApenas números, por favor!\n')