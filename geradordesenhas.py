import string
import random

def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da senha: "))
    senha = gerar_senha(tamanho)
    print(f"Sua senha gerada é: {senha}")

