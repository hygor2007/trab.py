import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_sabores():
    sabores = ["Chocolate", "Morango", "Baunilha", "Floresta Negra"]
    print("Sabores disponíveis:")
    for i, sabor in enumerate(sabores, 1):
        print(f"{i}. {sabor}")
    return sabores

def coleta_dados_entrega():
    rua = input("Digite o nome da rua: ")
    numero = input("Digite o número: ")
    return rua, numero

def novo_pedido(pedidos):
    limpar_tela()
    print("\n--- Novo Pedido ---")
    compra(pedidos)

def compra(pedidos):
    while True:
        sabores = menu_sabores()
        escolha = int(input("Qual sabor vai querer? (Digite o número): "))
        sabor_escolhido = sabores[escolha - 1]
        print(f"Sabor escolhido: {sabor_escolhido}")

        print("Escolha a forma de pagamento:")
        print("1. Cartão")
        print("2. Dinheiro")
        pagamento_opcao = int(input("Digite o número da opção: "))
        pagamento = "Cartão" if pagamento_opcao == 1 else "Dinheiro"

        entrega = input("É para entrega? (Sim/Não): ")

        if entrega.lower() == "sim":
            rua, numero = coleta_dados_entrega()
            endereco = f"{rua}, Nº {numero}"
            print(f"Endereço de entrega: {endereco}")
        else:
            endereco = "Retirada no local"

        pedido = {
            'sabor': sabor_escolhido,
            'pagamento': pagamento,
            'entrega': entrega,
            'endereco': endereco
        }
        pedidos.append(pedido)

        print("Compra concluída!")
        print(f"Sabor: {sabor_escolhido}, Pagamento: {pagamento}, Entrega: {entrega}")

        continuar = input("Deseja abrir um novo pedido? (Sim/Não): ")
        if continuar.lower() == "sim":
            novo_pedido(pedidos)
            break
        else:
            break

if __name__ == "__main__":
    pedidos = []
    novo_pedido(pedidos)
    print("\n--- Pedidos Realizados ---")
    for p in pedidos:
        print(p)
