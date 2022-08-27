saque = int(input('Digite o valor que deseja sacar: '))
cinquenta = 50
vinte = 20
dez = 10
um = 1

contagemVinte = 0
contagemDez = 0
contagemUm = 0
contagem = saque // cinquenta
print(contagem)
sobra = saque % cinquenta

while sobra != 0:
    if sobra >= vinte and sobra < 50:
        contagemVinte = sobra // 20
        sobra = sobra % vinte
    elif sobra < vinte and sobra >= 10:
        contagemDez = sobra // 10
        sobra = sobra % 10
    elif sobra < dez:
        contagemUm = sobra // 1
        sobra = sobra % 1


print(f' Para a quantia de R${saque},00 será necessário: {contagem} cédulas de R$50,00,\n'
      f' {contagemVinte} cédulas de R$20,00\n {contagemDez} cédulas de R$10,00\n e {contagemUm} cédulas de R$1,00.')


