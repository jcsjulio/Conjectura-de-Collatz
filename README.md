🔢 Conjectura de Collatz



Uma implementação da Conjectura de Collatz em Python.

O programa recebe um número inteiro positivo informado pelo usuário, aplica as regras da conjectura até chegar ao número 1, exibe cada etapa do processo, gera a sequência completa e informa o total de passos necessários.

📖 O que é a Conjectura de Collatz?
A Conjectura de Collatz, também conhecida como Problema 3n + 1, foi proposta pelo matemático alemão Lothar Collatz em 1937.

O algoritmo segue duas regras simples:

🔹 Se o número for par, divida-o por 2.
🔹 Se o número for ímpar, multiplique-o por 3 e some 1.
Essas operações são repetidas até que o número seja igual a 1.

Apesar de ter sido testada para números extremamente grandes por meio de computadores, até hoje não existe uma demonstração matemática que prove que isso acontece para todos os números inteiros positivos.

✨ Funcionalidades
✅ Recebe um número inteiro positivo.
✅ Valida entradas inválidas.
✅ Exibe cada passo da execução.
✅ Mostra a operação realizada em cada iteração.
✅ Gera a sequência completa.
✅ Calcula a quantidade total de passos até chegar ao número 1.
💻 Exemplo de execução
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

📂 Estrutura do projeto
Conjectura-de-Collatz/
│
├── conjectura.py
└── README.md

🚀 Como executar
1. Clone o repositório
git clone https://github.com/jcsjulio/Conjectura-de-Collatz.git

2. Entre na pasta do projeto
cd Conjectura-de-Collatz

3. Execute o programa
python conjectura.py

ou, dependendo da instalação do Python:

python3 conjectura.py

🛠️ Tecnologias utilizadas
Python 3
🎯 Objetivo
Este projeto foi desenvolvido como exercício de programação para demonstrar:

Estruturas de repetição (while);
Estruturas condicionais (if e else);
Manipulação de listas;
Criação de funções;
Entrada e saída de dados;
Organização de código seguindo boas práticas em Python.
📚 Referências
https://pt.wikipedia.org/wiki/Conjectura_de_Collatz
https://en.wikipedia.org/wiki/Collatz_conjecture
👨‍💻 Autor
Julio César

GitHub: https://jcsjulio.github.io/

📄 Licença
Este projeto é de uso educacional e foi desenvolvido com o objetivo de praticar lógica de programação e Python.

Na minha opinião, esse README tem um padrão bem próximo ao encontrado em projetos open source: usa badges, organiza o conteúdo por seções, explica o contexto matemático, mostra um exemplo de execução e descreve a estrutura do projeto e como executá-lo. Isso deixa o repositório mais completo e agradável para quem o visita.