from conta_bancaria import ContaBancaria


def main():
    print("Bem-vindo ao Banco Python!")
    titular = input("Digite o nome do titular da conta: ")
    senha = input("Crie uma senha para sua conta: ")
    conta = ContaBancaria(titular, senha)

    while True:
        print("\nEscolha uma operação:")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Alterar Senha")
        print("5. Sair")

        opcao = input("Digite o número da operação desejada: ")

        if opcao == "1":
            senha = input("Digite sua senha: ")
            print(conta.consultar_saldo(senha))
        
        elif opcao == "2":
            valor = float(input("Digite o valor a ser depositado: "))
            print(conta.depositar(valor))
        
        elif opcao == "3":
            valor = float(input("Digite o valor a ser sacado: "))
            senha = input("Digite sua senha: ")
            print(conta.sacar(valor, senha))
        
        elif opcao == "4":
            senha_atual = input("Digite sua senha atual: ")
            nova_senha = input("Digite a nova senha: ")
            print(conta.alterar_senha(senha_atual, nova_senha))
        
        elif opcao == "5":
            print("Obrigado por usar o Banco Python!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
