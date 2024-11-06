-py-
import os
import json

# Função para limpar a tela (depende do sistema operacional)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir o menu de sabores
def menu_sabores(valores):
    sabores = list(valores.keys())  # Pegamos apenas as chaves (sabores)
    print("Sabores disponíveis:")
    for i, sabor in enumerate(sabores, 1):
        valor = valores.get(sabor, 0)
        print(f"{i}. {sabor} (Preço: R$ {valor:.2f})")
    return sabores

# Função para coleta de dados de entrega
def coleta_dados_entrega():
    rua = input("Digite o nome da rua: ")
    numero = input("Digite o número: ")
    return rua, numero

# Função para salvar os pedidos no arquivo 'pedidos.json'
def salvar_pedidos(pedidos):
    try:
        with open('pedidos.json', 'w') as file:
            json.dump(pedidos, file, indent=4)
    except Exception as e:
        print(f"Erro ao salvar pedidos: {e}")

# Função para carregar pedidos do arquivo 'pedidos.json'
def carregar_pedidos():
    if os.path.exists('pedidos.json'):
        try:
            with open('pedidos.json', 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de pedidos. O arquivo pode estar corrompido.")
            return []
    return []

# Função para salvar o valor dos sabores no arquivo 'valores.json'
def salvar_valores(valores):
    try:
        with open('valores.json', 'w') as file:
            json.dump(valores, file, indent=4)
    except Exception as e:
        print(f"Erro ao salvar valores: {e}")

# Função para carregar os valores dos sabores do arquivo 'valores.json'
def carregar_valores():
    if os.path.exists('valores.json'):
        try:
            with open('valores.json', 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de valores. O arquivo pode estar corrompido.")
            return {}
    # Se o arquivo não existir, retorna valores iniciais com preços
    return {
        "Chocolate": 10.00,
        "Morango": 8.50,
        "Baunilha": 7.00,
        "Floresta Negra": 12.00,
        "Limão": 6.00,
        "Coco": 9.00,
        "Pistache": 15.00,
        "Caramelo": 11.00,
    }

# Função para processar o novo pedido
def novo_pedido(pedidos, valores):
    limpar_tela()
    print("\n--- Novo Pedido ---")
    compra(pedidos, valores)

# Função de compra
def compra(pedidos, valores):
    while True:
        sabores = menu_sabores(valores)
        try:
            escolha = int(input("\nQual sabor vai querer? : "))
            if escolha < 1 or escolha > len(sabores):
                print("Opção inválida. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue

        sabor_escolhido = sabores[escolha - 1]

        # Adicionando R$ 3,00 ao preço de cada sabor
        preco_sabor = valores[sabor_escolhido] + 3.00

        try:
            quantidade = int(input(f"Quantos de {sabor_escolhido} você deseja? (Preço por unidade: R$ {preco_sabor:.2f}): "))
            if quantidade <= 0:
                print("Quantidade inválida. Tente novamente.")
                continue
        except ValueError:
            print("Por favor, insira um número válido para a quantidade.")
            continue

        print(f"Sabor escolhido: {sabor_escolhido}, Quantidade: {quantidade}")
        
        # Calculando o valor total da compra
        valor_total = preco_sabor * quantidade
        print(f"Valor total para {quantidade} x {sabor_escolhido}: R$ {valor_total:.2f}")

        print("Escolha a forma de pagamento:")
        print("1. Cartão")
        print("2. Dinheiro")
        try:
            pagamento_opcao = int(input("Digite o número da opção: "))
            pagamento = "Cartão" if pagamento_opcao == 1 else "Dinheiro"
        except ValueError:
            print("Opção inválida. Considerando como 'Dinheiro'.")
            pagamento = "Dinheiro"

        entrega = input("É para entrega? (Sim/Não): ")

        if entrega.lower() == "sim":
            rua, numero = coleta_dados_entrega()
            endereco = f"{rua}, Nº {numero}"
            print(f"Endereço de entrega: {endereco}")
        else:
            endereco = "Retirada no local"

        pedido = {
            'sabor': sabor_escolhido,
            'quantidade': quantidade,
            'valor_total': valor_total,
            'pagamento': pagamento,
            'entrega': entrega,
            'endereco': endereco
        }
        pedidos.append(pedido)

        salvar_pedidos(pedidos)
        salvar_valores(valores)

        print("Compra concluída!")
        print(f"Sabor: {sabor_escolhido}, Quantidade: {quantidade}, Pagamento: {pagamento}, Entrega: {entrega}")
        print(f"Valor Total: R$ {valor_total:.2f}")

        continuar = input("Deseja abrir um novo pedido? (Sim/Não): ")
        if continuar.lower() == "sim":
            novo_pedido(pedidos, valores)
            break
        else:
            break

# Função para acessar o último pedido realizado
def acessar_pedidos(pedidos):
    if not pedidos:
        print("Nenhum pedido encontrado.")
    else:
        p = pedidos[-1]  # Pega o último pedido
        print("\n--- Último Pedido Realizado ---")
        print(f"  Sabor: {p['sabor']}, Quantidade: {p['quantidade']}")
        print(f"  Valor Total: R$ {p['valor_total']:.2f}")
        print(f"  Pagamento: {p['pagamento']}")
        print(f"  Entrega: {p['entrega']}")
        if p['entrega'].lower() == "sim":
            print(f"  Endereço: {p['endereco']}")
        print()

# Programa principal
if __name__ == "__main__":
    pedidos = carregar_pedidos()
    valores = carregar_valores()

    while True:
        limpar_tela()

        print("1. Novo Pedido")
        print("2. Acessar Último Pedido")
        print("3. Sair")

        try:
            opcao = int(input("Escolha uma opção:"))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

        if opcao == 1:
            novo_pedido(pedidos, valores)
        elif opcao == 2:
            acessar_pedidos(pedidos)
            input("Pressione Enter para continuar...")
        elif opcao == 3:
            break
        else:
            print("Opção inválida! Tente novamente.")


-js-
const http = require('http');
const fs = require('fs');
const path = require('path');
const porta = 3000;
const filePath = path.join(__dirname, 'estoque.json');

// Função para ler o arquivo de estoque
function lerArquivo() {
    try {
        const data = fs.readFileSync(filePath, 'utf8'); // Lê o arquivo de forma síncrona
        return JSON.parse(data); // Converte o conteúdo para JSON
    } catch (erro) {
        console.error('Erro ao ler o arquivo:', erro);
        return null; // Retorna null em caso de erro
    }
}

// Criação do servidor HTTP
const server = http.createServer((req, res) => {
    if (req.url === '/estoque' && req.method === 'GET') {
        const estoque = lerArquivo();
        if (estoque) {
            res.statusCode = 200;
            res.setHeader('Content-Type', 'application/html');
            res.end(estoque.Chocolate+"<br/>"+estoque.morango); // Retorna o estoque como JSON
        
        } else {
            res.statusCode = 500;
            res.setHeader('Content-Type', 'text/plain');
            res.end('Erro ao carregar o estoque');
        }
    } else {
        res.statusCode = 404;
        res.setHeader('Content-Type', 'text/plain');
        res.end('Rota não encontrada');
    }
});

// Inicia o servidor
server.listen(porta, () => {
    console.log(`Servidor rodando em http://localhost:${porta}/estoque`);
});





{
    "Chocolate": 1.0,
    "Morango": 1.5,
    "Baunilha": 1.0,
    "Floresta Negra": 1.0,
    "Lim\u00e3o": 1.0,
    "Coco": 1.0,
    "Pistache": 1.0,
    "Caramelo": 1.0
}
