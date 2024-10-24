opcao = int(input("Selecione uma opção: \n[1] Registrar-se \n[2] Sacar \n[3] Ver saldo \n[4] Depositar \n[5] Ver extrato \n[6] Sair  "))
usuarios = {}  # Dicionário para armazenar usuários e senhas
operacoes = []
qtd_saques_diarios = 0
saldo = 2000.0

while opcao != 6:
    if opcao == 1:
        cadastro_usuario = input("Cadastre um Nome de Usuário: ").strip()
        if cadastro_usuario in usuarios:
            print("Usuário já cadastrado!")
        else:
            cadastro_senha = input("Cadastre uma senha: ")
            usuarios[cadastro_usuario] = cadastro_senha  # Armazena usuário e senha
            print("Cadastro concluído com sucesso!")

    elif opcao == 2:
        user = input("Digite seu Nome de Usuário: ").strip()
        if user in usuarios:  # Verifica se o usuário existe
            senha = input("Digite sua senha: ")
            if senha == usuarios[user]:  # Compara com a senha armazenada
                saque = float(input("Informe o valor do saque: "))
                if saldo >= saque:
                    if qtd_saques_diarios < 3:
                        if saque <= 500:
                            saldo -= saque
                            qtd_saques_diarios += 1
                            print("Saque realizado!")
                            print(f"Seu saldo é: R$ {saldo:.2f}")
                            operacoes.append(f"\n- R${saque:.2f}")
                        else:
                            print("Limite de saque excedido.")
                    else:
                        print("Limite de saques diários atingido.")
                else:
                    print("Saldo insuficiente.")
                    print(f"Seu saldo é R$ {saldo:.2f}")
            else:
                print("Senha inválida.")
        else:
            print("Usuário inexistente.")

    elif opcao == 3:
        print(f"Seu saldo é R$ {saldo:.2f}")

    elif opcao == 4:
        user = input("Digite seu Nome de Usuário: ").strip()
        if user in usuarios:
            senha = input("Digite sua senha: ")
            if senha == usuarios[user]:
                while True:
                    deposito = float(input("Digite o valor que deseja depositar: "))
                    if deposito > 0:
                        saldo += deposito
                        print(f"Seu saldo é R$ {saldo:.2f}")
                        operacoes.append(f"\n+ R${deposito:.2f}")
                        break
                    else:
                        print("Valor inválido. Tente novamente.")
            else:
                print("Senha inválida.")
        else:
            print("Usuário inexistente.")

    elif opcao == 5:
        if not operacoes:
            print("Nenhuma operação foi realizada.")
        else:
            print("Extrato:")
            for op in operacoes:
                print(op)

    else:
        print("Opção inválida!")

    opcao = int(input("Selecione uma opção: \n[1] Registrar-se \n[2] Sacar \n[3] Ver saldo \n[4] Depositar \n[5] Ver extrato \n[6] Sair  "))
