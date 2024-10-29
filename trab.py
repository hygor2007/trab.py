--py--

import os
import json

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_sabores(estoque):
    sabores = ["Chocolate", "Morango", "Baunilha", "Floresta Negra", "Limão", "Coco", "Pistache", "Caramelo"]
    print("Sabores disponíveis:")
    for i, sabor in enumerate(sabores, 1):
        quantidade = estoque.get(sabor, 0)
        print(f"{i}. {sabor} (Estoque: {quantidade})")
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

def salvar_estoque(estoque):
    with open('estoque.json', 'w') as file:
        json.dump(estoque, file)

def carregar_estoque():
    if os.path.exists('estoque.json'):
        with open('estoque.json', 'r') as file:
            return json.load(file)
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

def novo_pedido(pedidos, estoque):
    limpar_tela()
    print("\n--- Novo Pedido ---")
    compra(pedidos, estoque)

def compra(pedidos, estoque):
    while True:
        sabores = menu_sabores(estoque)
        escolha = int(input("\nQual sabor vai querer? : "))
        sabor_escolhido = sabores[escolha - 1]
        
        if estoque[sabor_escolhido] <= 0:
            print(f"Desculpe, {sabor_escolhido} está fora de estoque.")
            continue

        quantidade = int(input(f"Quantos de {sabor_escolhido} você deseja? (Estoque disponível: {estoque[sabor_escolhido]}): "))
        
        if quantidade > estoque[sabor_escolhido] or quantidade <= 0:
            print("Quantidade inválida. Tente novamente.")
            continue

        print(f"Sabor escolhido: {sabor_escolhido}, Quantidade: {quantidade}")

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

def gerenciar_estoque(estoque):
    while True:
        print("\n--- Gerenciamento de Estoque ---")
        print("1. Adicionar Estoque")
        print("2. Remover Estoque")
        print("3. Voltar")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            sabor = input("Digite o sabor a adicionar: ")
            quantidade = int(input("Digite a quantidade a adicionar: "))
            if sabor in estoque:
                estoque[sabor] += quantidade
                print(f"Estoque de {sabor} atualizado para {estoque[sabor]}.")
            else:
                print("Sabor não encontrado.")
        elif opcao == 2:
            sabor = input("Digite o sabor a remover: ")
            quantidade = int(input("Digite a quantidade a remover: "))
            if sabor in estoque and estoque[sabor] >= quantidade:
                estoque[sabor] -= quantidade
                print(f"Estoque de {sabor} atualizado para {estoque[sabor]}.")
            else:
                print("Quantidade inválida ou sabor não encontrado.")
        elif opcao == 3:
            salvar_estoque(estoque)
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    pedidos = carregar_pedidos()
    estoque = carregar_estoque()
    
    while True:
        limpar_tela()
        print("1. Novo Pedido")
        print("2. Acessar Último Pedido")
        print("3. Gerenciar Estoque")
        print("4. Sair")
        opcao = int(input("Escolha uma opção: "))
        
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









----js-----


const http = require('http');
const fs = require('fs');
const porta = 3000;
const filePath = 'estoque.json';

function lerarquivo(){
    try {
        const data = fs.readFileSync(filePath, 'utf8'); // Lê o arquivo de forma síncrona 
        const jsonData = JSON.parse(data); // Converte o conteúdo para JSON 
        return jsonData; // Retorna os dados
    }
    catch (erro) { 
        console.error('Erro ao ler o arquivo:', erro); 
        return null; // Retorna null em caso de erro
    } 
}

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');
    estoque = lerarquivo();
    console.log(estoque);
    res.end("<a>"+estoque.nome+"</a>");
})

server.listen(porta, () => {
    console.log(`Servidor rodando em http://localhost:${porta}/`);
})

/*
function carregarEstoque() {
    try {
        const data = fs.readFileSync(filePath, 'utf8');
        return JSON.parse(data);
    } catch (error) {
        console.error('Erro ao carregar o estoque:', error);
        return {
            //Estoque padrão
        };
    }
}

function criarResposta(res, statusCode, contentType, data) {
    res.statusCode = statusCode;
    res.setHeader('Content-Type', contentType);
    //const estoque = carregarEstoque();
    //console.log(estoque);
    res.end("oi");
}

const server = http.createServer((req, res) => {
    if (req.url === '/estoque' && req.method === 'GET') {
       //const estoque = carregarEstoque();
        criarResposta(res, 200, 'application/json', e);
    } else {
        criarResposta(res, 404, 'text/plain', { error: 'Rota não encontrada' });
    }
});

server.listen(porta, () => {
    console.log(`Servidor rodando em http://localhost:${porta}/estoque`);
});*/





{
    "nome": "hygor"
}
