'''Faça um Programa que converta metros para centímetros'''

# CÓDIGO QUEBRADO

while True:
        menu = int(input('Bem-vindo ao conversor de medidas!\nO que deseja converter?\n[1] Metros em centímetros\n[2] Centímetros em metros\n[3] Sair\nDigite sua opção: '))
        if menu == 3:
            print('Até a próxima!')
            exit()
        elif menu >= 1 or menu <= 2:
            match menu:
                case 1:
                    calc_ctms = float(input('Digite o valor em metro(s) a converter: '))
                    print(f'Convertendo {calc_ctms} metro(s) para centímetro(s) obtemos: {calc_ctms * 100} centímetros')
                case 2:
                    calc_mts = float(input('Valor em centímetro(s) a converter: '))
                    print(f'Convertendo {calc_mts} centímetro(s) para metro(s) obtemos: {calc_mts / 100}')
                case _:
                    print('Opção inválida. Tente novamente.')
        else:
             print('Opção inválida. Tente novamente.')