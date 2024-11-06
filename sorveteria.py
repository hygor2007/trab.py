-py-
import os
import json

# Função para limpar a tela (depende do sistema operacional)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir o menu de sabores
def menu_sabores(estoque):
    sabores = ["Chocolate", "Morango", "Baunilha", "Floresta Negra", "Limão", "Coco", "Pistache", "Caramelo"]
    print("Sabores disponíveis:")
    for i, sabor in enumerate(sabores, 1):
        quantidade = estoque.get(sabor, 0)
        print(f"{i}. {sabor} (Estoque: {quantidade})")
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

# Função para salvar o estoque no arquivo 'estoque.json'
def salvar_estoque(estoque):
    try:
        with open('estoque.json', 'w') as file:
            json.dump(estoque, file, indent=4)
    except Exception as e:
        print(f"Erro ao salvar estoque: {e}")

# Função para carregar o estoque do arquivo 'estoque.json'
def carregar_estoque():
    if os.path.exists('estoque.json'):
        try:
            with open('estoque.json', 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de estoque. O arquivo pode estar corrompido.")
            return {}
    return {
        "Chocolate": 10,
        "Morango": 10,
        "Baunilha": 10,
        "Floresta Negra": 10,
        "Limão": 10,
        "Coco": 10,
        "Pistache": 10,
        "Caramelo": 10,
    }

# Função para processar o novo pedido
def novo_pedido(pedidos, estoque):
    limpar_tela()
    print("\n--- Novo Pedido ---")
    compra(pedidos, estoque)

# Função de compra
def compra(pedidos, estoque):
    while True:
        sabores = menu_sabores(estoque)
        try:
            escolha = int(input("\nQual sabor vai querer? : "))
            if escolha < 1 or escolha > len(sabores):
                print("Opção inválida. Tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")
            continue

        sabor_escolhido = sabores[escolha - 1]

        # Verificar se há estoque suficiente
        if estoque[sabor_escolhido] <= 0:
            print(f"Desculpe, {sabor_escolhido} está fora de estoque.")
            continue

        try:
            quantidade = int(input(f"Quantos de {sabor_escolhido} você deseja? (Estoque disponível: {estoque[sabor_escolhido]}): "))
            if quantidade > estoque[sabor_escolhido] or quantidade <= 0:
                print("Quantidade inválida. Tente novamente.")
                continue
        except ValueError:
            print("Por favor, insira um número válido para a quantidade.")
            continue

        print(f"Sabor escolhido: {sabor_escolhido}, Quantidade: {quantidade}")

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
            'pagamento': pagamento,
            'entrega': entrega,
            'endereco': endereco
        }
        pedidos.append(pedido)

        # Atualizar estoque
        estoque[sabor_escolhido] -= quantidade
        salvar_pedidos(pedidos)
        salvar_estoque(estoque)

        print("Compra concluída!")
        print(f"Sabor: {sabor_escolhido}, Quantidade: {quantidade}, Pagamento: {pagamento}, Entrega: {entrega}")

        continuar = input("Deseja abrir um novo pedido? (Sim/Não): ")
        if continuar.lower() == "sim":
            novo_pedido(pedidos, estoque)
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
        print(f"  Pagamento: {p['pagamento']}")
        print(f"  Entrega: {p['entrega']}")
        if p['entrega'].lower() == "sim":
            print(f"  Endereço: {p['endereco']}")
        print()

# Função para gerenciar o estoque (adicionar e remover itens)
def gerenciar_estoque(estoque):
    while True:
        print("\n--- Gerenciamento de Estoque ---")
        print("1. Adicionar Estoque")
        print("2. Remover Estoque")
        print("3. Voltar")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            sabor = input("Digite o sabor a adicionar: ")
            try:
                quantidade = int(input("Digite a quantidade a adicionar: "))
                if sabor in estoque:
                    estoque[sabor] += quantidade
                    print(f"Estoque de {sabor} atualizado para {estoque[sabor]}.")
                else:
                    print("Sabor não encontrado.")
            except ValueError:
                print("Por favor, insira um número válido para a quantidade.")
        elif opcao == 2:
            sabor = input("Digite o sabor a remover: ")
            try:
                quantidade = int(input("Digite a quantidade a remover: "))
                if sabor in estoque and estoque[sabor] >= quantidade:
                    estoque[sabor] -= quantidade
                    print(f"Estoque de {sabor} atualizado para {estoque[sabor]}.")
                else:
                    print("Quantidade inválida ou sabor não encontrado.")
            except ValueError:
                print("Por favor, insira um número válido para a quantidade.")
        elif opcao == 3:
            salvar_estoque(estoque)
            break
        else:
            print("Opção inválida! Tente novamente.")

# Programa principal
if __name__ == "__main__":
    pedidos = carregar_pedidos()
    estoque = carregar_estoque()

    while True:
        limpar_tela()

        print("1. Novo Pedido")
        print("2. Acessar Último Pedido")
        print("3. Gerenciar Estoque")
        print("4. Sair")

        try:
            opcao = int(input("Escolha uma opção:"))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            continue

        if opcao == 1:
            novo_pedido(pedidos, estoque)
        elif opcao == 2:
            acessar_pedidos(pedidos)
            input("Pressione Enter para continuar...")
        elif opcao == 3:
            gerenciar_estoque(estoque)
        elif opcao == 4:
            salvar_estoque(estoque)
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
            res.setHeader('Content-Type', 'application/json');
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
    "Chocolate": 7,
    "Morango": 10,
    "Baunilha": 10,
    "Floresta Negra": 10,
    "Lim\u00e3o": 10,
    "Coco": 10,
    "Pistache": 10,
    "Caramelo": 10
}
