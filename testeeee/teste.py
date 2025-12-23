print("BEMVINDO AO SISTEMA BANCARIO\n")

saldo = 10000


while True:

    print("Seu saldo é R${:.2f}".format(saldo))
    opc_menu = int(input("digite a opcao:\n [0]DEPOSITAR\n [1]TRANSFERIR\n [2]SAIR\n "))

    match opc_menu:
        case 0:
            print("Opçao escolhida DEPOSITAR")
            valor_deposito = float(input("Qual valor deseja despositar: "))

            saldo = valor_deposito + saldo

            print("Seu saldo atualizado é: R${:.2f}".format(saldo))

        case 1:
            print("Opcao escolhida TRANSFERIR")
            chave_pix = str(input("Digite a chave pix: "))
            valor_trans = float(input("Digite o valor a ser transferido: R$ "))

            print("Pix realizado! A chave {} recebeu R${}!".format(chave_pix, valor_trans))

            saldo = saldo - valor_trans
            print("O seu saldo é de: R${}".format(saldo))
                
        case 2:
            print("Obrigado por utilizar nosso sistema")
            break
