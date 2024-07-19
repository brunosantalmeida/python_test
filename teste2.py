faturamento = 1200
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento
print(f"Faturamento da empresa: {faturamento}, Custo: {custo}, Lucro: {lucro}")

email_cliente = "lira@gmail.com"

# minuscula
email_cliente = email_cliente.upper()
print(email_cliente)
#minuscula
email_cliente = email_cliente.lower()
print(email_cliente)


print(email_cliente.find("@")) # -1 quando nao encontrar

# tamanho do texto 
print(len(email_cliente))

# pegar um caractere
print(email_cliente[4])

print(email_cliente[-4])

# pegar um pedaço do texto
print(email_cliente[4:])

# troca um pedaço do texto
novo_email = email_cliente.replace("gmail.com" , "hotmail.com")
print(novo_email)

nome = "joao lira"
# trabalher com nomes

print(nome.capitalize())
print(nome.title())

# pegar o servidor do email
posicao_arroba = email_cliente.find("@") + 1
servidor = email_cliente[posicao_arroba:]
print(servidor)
# pegaro 1º nome
posicao_espaco = nome.find(" ")
primeiro_nome = nome[:posicao_espaco]

# pegar o sobrenome
sobrenome = nome [posicao_espaco+1:]
print(primeiro_nome)
print(sobrenome)

# caso especiais
margem_lucro = round(margem_lucro, 2)
print(f"Faturamento da empresa: {faturamento:.2f}, Custo: {custo}, Lucro: {lucro}, Margem: {margem_lucro: .0%}")