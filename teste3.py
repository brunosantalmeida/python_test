# inputs



# faturamento = float(input("Escreva o faturamento:"))

# imposto = faturamento * 0.1
# print(imposto)



# listas
vendas = [100, 50, 14, 20, 30, 700]

# soma dos elementos
total_vendas = sum(vendas)
print(total_vendas)

#tamanho da lista 
quantidade_venda = len(vendas)
print(quantidade_venda)

# max e min
print(max(vendas))
print(min(vendas))

# pega a posicão
print(vendas[5])

lista_produtos = ["iphone", "aipod", "ipad", "macbook"]

# produto_procurado = input("pesquise pelo nome do produto: ")
# produto_procurado = produto_procurado.lower()

# print(produto_procurado in lista_produtos)

#adicionar um item
lista_produtos.append("apple watch")
print(lista_produtos)


#remover um item
lista_produtos.remove("apple watch")
print(lista_produtos)
#editar um item
precos = [1000, 1500, 3500]
precos[0] = precos[0] * 1.5
print(precos)
#contar quatas vezes um item aparecer na lista 
lista_produtos = ["iphone", "aipod", "ipad", "macbook", "iphone", "ipad", "iphone"]

print(lista_produtos.count("apple watch"))
                  


# ordenar um lista 

lista_produtos.sort(reverse=True)
print(vendas)