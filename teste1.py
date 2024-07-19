faturamento = 1200 # tipo : int -> numero intero 
custo = 750.0 # tipo : flout -> numero com casa decimal

novas_vendas =100
faturamento = faturamento + novas_vendas
imposto = faturamento * 0.1

lucro = faturamento - custo - imposto


margem_lucro = lucro / faturamento

print("Faturamento foi de ",faturamento)
print("o custo foi de ", custo)
print("O lucro foi de ",lucro)
print("A margem de lucro foi de", round (margem_lucro,1))

mensagem = "O faturamento da loja foi de tanto"#
email = "emailqualquer@gmail.com" # tipo string -> texto

teve_lucro = True # variavel boolean

# Mod -> % resto da divisao
tempo_contrato = 170
tempo_anos = 170 / 12
tempo_meses = 170 % 12
print("Tempo em messes", tempo_meses)