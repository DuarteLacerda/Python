import random

cumprimento = int(input("Digite o cumprimento da senha: "))
senha = ''
for i in range(cumprimento):
    senha += chr(random.randint(33, 126))
print(senha)