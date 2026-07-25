# 🔢 Conjectura de Collatz

Uma implementação da **Conjectura de Collatz** em **Python**. O programa recebe um número inteiro positivo, valida a entrada, gera toda a sequência da conjectura, exibe cada etapa da execução e informa a quantidade total de passos até chegar ao número **1**.

---

## 📖 O que é a Conjectura de Collatz?

A **Conjectura de Collatz**, também conhecida como **Problema 3n + 1**, foi proposta pelo matemático **Lothar Collatz** em 1937.

O algoritmo segue duas regras simples:

- Se o número for **par**, divida-o por **2**.
- Se o número for **ímpar**, multiplique-o por **3** e some **1**.

Essas operações são repetidas até que o número seja igual a **1**.

Apesar de ter sido testada para números extremamente grandes por meio de computadores, ainda não existe uma demonstração matemática que prove que isso acontece para todos os números inteiros positivos.

---

## ✨ Funcionalidades

- ✅ Recebe um número inteiro positivo.
- ✅ Valida entradas inválidas.
- ✅ Exibe cada passo da execução.
- ✅ Mostra a operação realizada em cada iteração.
- ✅ Gera a sequência completa.
- ✅ Calcula o total de passos até chegar ao número 1.

---

## 💻 Exemplo de execução

```text
=========================================
         Conjectura de Collatz
=========================================

Digite um número inteiro positivo: 6

Passo 1: 6 é par -> 6 / 2 = 3
Passo 2: 3 é ímpar -> 3 × 3 + 1 = 10
Passo 3: 10 é par -> 10 / 2 = 5
Passo 4: 5 é ímpar -> 5 × 3 + 1 = 16
Passo 5: 16 é par -> 16 / 2 = 8
Passo 6: 8 é par -> 8 / 2 = 4
Passo 7: 4 é par -> 4 / 2 = 2
Passo 8: 2 é par -> 2 / 2 = 1

Sequência gerada:
6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

Total de passos: 8
```

---

## 📂 Estrutura do projeto

```text
Conjectura-de-Collatz/
│
├── conjectura.py
└── README.md
```

---

## 🚀 Como executar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/jcsjulio/Conjectura-de-Collatz.git
```

### 2️⃣ Acesse a pasta do projeto

```bash
cd Conjectura-de-Collatz
```

### 3️⃣ Execute o programa

```bash
python conjectura.py
```

ou

```bash
python3 conjectura.py
```

---

## 🛠️ Tecnologias utilizadas

- Python 3

---

## 📚 Conceitos praticados

Este projeto foi desenvolvido para praticar:

- Estruturas de repetição (`while`)
- Estruturas condicionais (`if` e `else`)
- Manipulação de listas
- Criação de funções
- Entrada e saída de dados
- Validação de dados
- Lógica de programação
- Algoritmos

---


## 👨‍💻 Autor

Desenvolvido por **Julio Cesar**.

Se este projeto foi útil para você, deixe uma ⭐ no repositório!