def fibonacci(n):
    fib_sequence = [0, 1]  # Inicializamos a sequência com os dois primeiros números
    for i in range(2, n):
        prox_num = fib_sequence[-1] + fib_sequence[-2]  # Calculamos o próximo número de Fibonacci
        fib_sequence.append(prox_num)  # Adicionamos o próximo número de Fibonacci à sequência
    return fib_sequence

# Exemplo de uso:
n_termos = int(input("Digite o número de termos da sequência de Fibonacci: "))
sequencia_fibonacci = fibonacci(n_termos)
print("Sequência de Fibonacci até {} termos:".format(n_termos))
print(sequencia_fibonacci)
