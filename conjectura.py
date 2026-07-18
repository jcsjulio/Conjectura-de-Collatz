def collatz(numero):
    sequencia = [numero]
    passos = 0

    print("\nPassos da Conjectura de Collatz:\n")

    while numero != 1:
        if numero % 2 == 0:
            proximo = numero // 2
            print(f"Passo {passos + 1}: {numero} é par -> {numero} / 2 = {proximo}")
        else:
            proximo = 3 * numero + 1
            print(f"Passo {passos + 1}: {numero} é ímpar -> 3 × {numero} + 1 = {proximo}")

        numero = proximo
        sequencia.append(numero)
        passos += 1

    return sequencia, passos


def main():
    print("=" * 45)
    print("         Conjectura de Collatz")
    print("=" * 45)

    numero = int(input("Digite um número inteiro positivo: "))

    if numero <= 0:
        print("Erro: o número deve ser positivo.")
        return

    sequencia, passos = collatz(numero)

    print("\n" + "=" * 45)
    print("Sequência gerada:")
    print(" -> ".join(map(str, sequencia)))
    print(f"\nTotal de passos: {passos}")


if __name__ == "__main__":
    main()