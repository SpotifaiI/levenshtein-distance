# Levenshtein Distance

# Equipe

* Cristian Prochnow
* Gustavo Henrique Dias
* Lucas Willian de Souza Serpa
* Marlon de Souza
* Ryan Gabriel Mazzei Bromati

## 📌 O Que o Código Faz?
Ele calcula a distância de edição (também chamada de Levenshtein Distance) entre duas strings.

Ou seja:

Qual o menor número de operações (inserir, deletar ou substituir caracteres) que eu preciso fazer para transformar uma string em outra?

Exemplo:

kitten → sitting precisa de 3 passos:

kitten → sitten (substitui 'k' por 's')

sitten → sittin (substitui 'e' por 'i')

sittin → sitting (insere 'g')

## 🤔 Por Que Usar Recursão com Memoization?
Se resolver isso de forma recursiva simples, a gente acaba recalculando MUITO as mesmas coisas.
A memoization resolve isso guardando os resultados anteriores num cache (usamos um dict em Python).

Assim a gente tem:

Recursividade → fácil de escrever e entender

Memoization → evita repetir cálculo → muito mais rápido

## ⚙️ Como Funciona?
🔄 Fluxo Geral:
Começamos do começo das duas strings.

Comparamos os caracteres atuais.

Se forem iguais → passamos pro próximo caractere de cada.

Se forem diferentes → tentamos:

Inserir (simula inserir um caractere da string 2 na string 1)

Deletar (remove um caractere da string 1)

Substituir (troca o caractere da string 1 pelo da string 2)

Calculamos o custo de cada operação e pegamos o menor.

## 🧠 E onde entra o cache?
Antes de fazer qualquer cálculo, a função vê se já tem o resultado guardado no memo[(i, j)].
Se tiver, ela retorna direto.
Se não tiver, ela calcula, guarda e então retorna.

