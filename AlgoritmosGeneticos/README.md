# Experimentos de otimização e algoritmos genéticos

Os experimentos de otimização e algoritmos genéticos serão adicionados conforme realizados (em aulas ou individuais).

São eles, até agora:


**A.01**: Busca aleatória

A busca aleatória é um algoritmo em que um certo espaço de busca é definido de onde sorteamos candidatos de soluções para o problema. Esse algoritmo não requer que a função objetivo seja diferenciável nem contínua.

Um algoritmo de busca aleatória segue os seguintes passos:

    · Um espaço de busca é definido

    · Um candidato dentro do espaço de busca é sorteado aleatoriamente

    · Calculamos o resultado da função objetivo para o candidato

    · Se o critério de parada for atingido, encerrar o algoritmo e retornar ao usuário o candidato que teve melhor resultado durante a busca. Do contrário, retorne ao passo 2


**A.02**: Busca em grade

A busca em grade testa exaustivamente todas as combinações possíveis entre um ou mais conjunto de parâmetros.
Para testar dois parâmetros em um problema de otimização, *p* e *q*. Os valores possíveis para *p* e *q* são: *p = {0, 1, 2}* e *q = {a, b, c}*

Em uma busca em grade, nós iremos testar todas as combinações entre *p* e *q*, sendo elas: *(0, a)*, *(0, b)*, *(0, c)*, *(1, a)*, *(1, b)*, *(1, c)*, *(2, a)*, *(2, b)* e *(2, c)*.

Um algoritmo de busca em grade segue os seguintes passos:

    · Definir quais são os parâmetros e quais são os valores possíveis para cada parâmetro

    · Computar e armazenar o resultado da função objetivo para todas as combinações possíveis dos parâmetros definidos no passo 1

    · Retornar ao usuário a combinação de parâmetros que teve o melhor resultado durante a busca.



**A.03**: Algoritmo genético

Algoritmos genéticos consistem em gerar uma população inicial aleatória e através de seleção, cruzamento e mutação sucessivas, gerar populações seguintes.
De forma simplificada, esse algoritmo segue os passos:

    · Criação da população inicial (aleatória)

    · Cálculo da função objetivo para todos os membros da população inicial e atualização do hall da fama

    · Seleção dos indivíduos (quais seguem pra próxima geração)

    · Cruzamento dos indivíduos selecionados (troca de material genético)

    · Mutação dos indivíduos da população recém-criada (possibilidade de trazer informação nova ao sistema)

    · Cálculo da função objetivo para todos os membros da população recém-criada e atualização do hall da fama

    · Checar os critérios de parada. Caso os critérios não tenham sido atendidos, retornar ao passo 3

    · Retornar para o usuário o hall da fama



**A.04**:
Em construção.

**A.05**:
Em construção.

**A.06**:
Em construção.

**A.07**:
Em construção.

**GA.01**:
Em construção.
