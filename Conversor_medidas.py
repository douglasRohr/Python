'''CONVERSOR DE MEDIDAS'''

# CÓDIGO QUEBRADO PARA INICIAR NO GIT

# CÓDIGO QUEBRA QUANDO O USUÁRIO INSERE LETRAS

while True:
    menu = int(input('''
Bem-vindo ao conversor de medidas!

O que deseja converter?
                                       
[1] Metros em centímetros
[2] Centímetros em metros
[3] Sair
                                         
Digite sua opção: '''))
    
    if menu == 3:
        print('Até a próxima!')
        exit()
    try:
        if menu >= 1 or menu <= 2: # APÓS O CÁLCULO, O CÓDIGO RETORNA AO MENU INDESEJADAMENTE
            match menu:
                case 1:
                    calc_ctms = float(input('Digite o valor em metro(s) a converter: '))
                    print(f'Convertendo {calc_ctms} metro(s) para centímetro(s) obtemos: {calc_ctms * 100} centímetros\n')
                case 2:
                    calc_mts = float(input('Valor em centímetro(s) a converter: '))
                    print(f'Convertendo {calc_mts} centímetro(s) para metro(s) obtemos: {calc_mts / 100}')
                case _:
                    print('Opção inválida. Tente novamente.')
    except:
        print('Opção inválida. Tente novamente.')