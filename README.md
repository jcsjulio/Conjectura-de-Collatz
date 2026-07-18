🔢 Conjectura de Collatz
Implementação da Conjectura de Collatz em Python.

O programa recebe um número inteiro positivo informado pelo usuário, aplica as regras da conjectura até chegar ao número 1, exibe cada passo da execução, mostra a sequência gerada e informa a quantidade total de passos.

Repositório: Conjectura-de-Collatz

📖 Sobre a Conjectura de Collatz
A Conjectura de Collatz, também conhecida como Problema 3n + 1, foi proposta pelo matemático Lothar Collatz em 1937. O problema consiste em aplicar as seguintes regras a qualquer número inteiro positivo:

Se o número for par, divida-o por 2.
Se o número for ímpar, multiplique-o por 3 e some 1.
Repita esse processo até que o número seja igual a 1.

Embora tenha sido verificada computacionalmente para valores extremamente grandes, até hoje não existe uma demonstração matemática que prove que isso acontece para todos os números inteiros positivos. 
W
Wikipédia

✨ Funcionalidades
Recebe um número inteiro positivo.
Exibe cada passo da execução.
Gera a sequência completa de Collatz.
Calcula a quantidade de passos necessários para chegar ao número 1.
Valida entradas inválidas.
▶️ Exemplo de execução
=============================================
         Conjectura de Collatz
=============================================
Digite um número inteiro positivo: 6

Passos da Conjectura de Collatz:

Passo 1: 6 é par -> 6 / 2 = 3
Passo 2: 3 é ímpar -> 3 × 3 + 1 = 10
Passo 3: 10 é par -> 10 / 2 = 5
Passo 4: 5 é ímpar -> 3 × 5 + 1 = 16
Passo 5: 16 é par -> 16 / 2 = 8
Passo 6: 8 é par -> 8 / 2 = 4
Passo 7: 4 é par -> 4 / 2 = 2
Passo 8: 2 é par -> 2 / 2 = 1

=============================================
Sequência gerada:
6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

Total de passos: 8


🛠️ Tecnologias utilizadas
Python 3


## 🚀 Como executar

### Clone o repositório

```bash
git clone https://github.com/jcsjulio/Conjectura-de-Collatz.git
```

### Acesse a pasta

```bash
cd Conjectura-de-Collatz
```

### Execute o programa

```bash
python conjectura.py
```

ou

```bash
python3 conjectura.py
```


## 📂 Estrutura do projeto

```text
Conjectura-de-Collatz/
│
├── conjectura.py
└── README.md
```

👨‍💻 Autor
Desenvolvido por Julio César.

GitHub: https://jcsjulio.github.io/