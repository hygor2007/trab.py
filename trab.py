import os
import json

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_sabores():
    sabores = ["Chocolate", "Morango", "Baunilha", "Floresta Negra"]
    print("Sabores disponíveis:")
    for i, sabor in enumerate(sabores, 1):
        print(f"{i}. {sabor}  ")
    return sabores

def coleta_dados_entrega():
    rua = input("Digite o nome da rua: ")
    numero = input("Digite o número: ")
    return rua, numero

def salvar_pedidos(pedidos):
    with open('pedidos.json', 'w') as file:
        json.dump(pedidos, file)

def carregar_pedidos():
    if os.path.exists('pedidos.json'):
        with open('pedidos.json', 'r') as file:
            return json.load(file)
    return []

def novo_pedido(pedidos):
    limpar_tela()
    print("\n--- Novo Pedido ---")
    compra(pedidos)

def compra(pedidos):
    while True:
        sabores = menu_sabores()
        escolha = int(input("\nQual sabor vai querer? : "))
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
        salvar_pedidos(pedidos)

        print("Compra concluída!")
        print(f"Sabor: {sabor_escolhido}, Pagamento: {pagamento}, Entrega: {entrega}" )

        continuar = input("Deseja abrir um novo pedido? (Sim/Não): ")
        if continuar.lower() == "sim":
            novo_pedido(pedidos)
            break
        else:
            break

def acessar_pedidos(pedidos):
    if not pedidos:
        print("Nenhum pedido encontrado.")
    else:
        ##mostre o pedido que foi feito
        p = pedidos[-1]  ## Pega o último pedido
        print("\n--- Último Pedido Realizado ---")
        print(f"  Sabor: {p['sabor']}")
        print(f"  Pagamento: {p['pagamento']}")
        print(f"  Entrega: {p['entrega']}")
        if p['entrega'].lower() == "sim":
            print(f"  Endereço: {p['endereco']}")
        print()  

if __name__ == "__main__":
    pedidos = carregar_pedidos()
    
    while True:
        limpar_tela()
        print("1. Novo Pedido")
        print("2. Acessar Último Pedido")
        print("3. Sair")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            novo_pedido(pedidos)
        elif opcao == 2:
            acessar_pedidos(pedidos)
            input("Pressione Enter para continuar...")
        elif opcao == 3:
            break
        else:
            print("Opção inválida! Tente novamente.")
