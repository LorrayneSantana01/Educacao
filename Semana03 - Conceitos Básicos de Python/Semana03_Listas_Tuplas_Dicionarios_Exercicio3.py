#Crie um dicionári o representando um carrinho de compras. Adicione produtos (chaves) e
#quantidades (valores) ao carrinho. Calcule o total do carrinho de compra.

carrinho = {}

carrinho["Amaciante"] = 2
carrinho["Papel Higênico"] = 12
carrinho["Desinfetante"] = 2
carrinho["Detergente"] = 4
carrinho["Cloro"] = 1

precos = {
    "Amaciante": 8.00,
    "Papel Higênico": 2.00,
    "Desinfetante": 10.00,
    "Detergente": 3.00,
    "Cloro": 15.00,
}

total = 0
for produto, quantidade in carrinho.items():
    total += precos[produto] * quantidade

print(f"Total do carrinho: R${total:.2f}")