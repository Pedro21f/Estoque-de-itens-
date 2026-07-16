
from tabulate import tabulate
from time import sleep

estoque = {
    '001': {
        'nome': 'Camisas',
        'marca': 'Nike',
        'quantidade': 50,
        'preço': 'R$21,99'
    },
    '002': {
        'nome': 'Calças',
        'marca': 'Adidas',
        'quantidade': 30,
        'preço': 'R$49,99'
    },
    '003': {
        'nome': 'Tênis',
        'marca': 'Converse',
        'quantidade': 20,
        'preço': 'R$79,99'
    },
    '004': {
        'nome': 'Sapatos',
        'marca': 'Puma',
        'quantidade': 25,
        'preço': 'R$99,99'
    },
    '005' : {
        'nome': 'Meias',
        'marca': 'Rebook',
        'quantidade': '74',
        'preço': 'R$7,99'
    }
}



while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Atualizar produto")
    print("4. Ver estoque")
    print("5. Sair do programa") 
    
    opção = input("Digite a opção desejada: ")
    if opção == "1":
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        marca = input("Digite a marca do produto: ")
        quantidade = int(input("Digite a quantidade do produto(em números inteiros): "))
        preço = float(input("Digite o preço do produto: "))
        
        # Salvando no dicionário
        estoque[codigo] = {
            'nome': nome,
            'marca': marca,
            'quantidade': quantidade,
            'preço': f"R${preço:.2f}"
        }
        print("Produto adicionado!")

    elif opção == "2":
        codigo = input("Digite o código do produto que deseja remover: ")
        if codigo in estoque:
            del estoque[codigo]
            print("Produto removido!")
        else:
            print("Produto não encontrado.")

    elif opção == "3":
        codigo = input("Digite o código do produto que deseja atualizar: ")
        if codigo in estoque:
            nome = input("Digite o novo nome do produto: ")
            marca = input("Digite a nova marca do produto: ")
            quantidade = int(input("Digite a nova quantidade do produto: "))
            preço = float(input("Digite o novo preço do produto: "))
            estoque[codigo] = {
                'nome': nome,
                'marca': marca,
                'quantidade': quantidade,
                'preço': f"R${preço:.2f}"
            }
            print("Produto atualizado!")
        else:
            print("Produto não encontrado.")    

    elif opção == "4":
        dados_tabela = []
        for codigo, info in estoque.items():
            dados_tabela.append([codigo, info['nome'], info['marca'], info['quantidade'], info['preço']])
        
        print(tabulate(dados_tabela, headers=['Código', 'Nome', 'Marca', 'Quantidade', 'Preço']))
        sleep(1)

    elif opção == "5":
        print("Encerrando o sistema... ")
        break 

    else:
        print("Opção inválida! Por favor, digite um número de 1 a 5.")
