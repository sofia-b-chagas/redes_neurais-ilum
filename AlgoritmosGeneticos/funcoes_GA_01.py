import random

def gene_sv(letras):
    """Sorteia uma letra
    Args:
        letras: letras ou símbolos possíveis de serem sorteados
    Returns:
        Retorna uma letra ou símbolo dentro dos possíveis de serem sorteados
    """
    
    return random.choice(letras)


def individuo_sv(tamanho_max, letras):
    """Cria um candidato para o problema da senha de tamanho variável
    Args:
        tamanho_max: tamanho máximo para a senha
        letras: letras possíveis de serem sorteadas
    Returns:
        Lista com n letras
    """
    
    candidato = []  
    tamanho = random.randint(3, tamanho_max)
    
    for _ in range(tamanho_max):        
        candidato.append(gene_sv(letras))
        
    return candidato


def populacao_inicial_sv(tamanho, letras):
    """Cria população inicial no problema da senha de tamanho variável
    Args:
        tamanho: tamanho da populção
        letras: letras possíveis de serem sorteadas
    Returns:
        Lista com todos os indivíduos da população no problema da senha
    """
    
    populacao = []
    
    for _ in range(tamanho):
        populacao.append(individuo_sv(tamanho, letras))
        
    return populacao


def funcao_objetivo_sv(individuo, senha_verdadeira, penalidade):
    """Computa a função objetivo de um indivíduo no problema da senha de tamanho variável
    Args:
      indivíduo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A distância entre a senha proposta e a senha verdadeira. Essa distância é medida letra por letra.
      Quanto mais distante uma letra for da que deveria ser, maior é essa distância
    """
    
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira):
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial))
       
    diferenca_tamanho = abs(len(individuo) - len(senha_verdadeira))
    diferenca += diferenca_tamanho * penalidade
    
    return diferenca


def funcao_objetivo_pop_sv(populacao, senha_verdadeira, penalidade):
    """Computa a função objetivo de uma populaçao no problema da senha de tamanho variável
    Args:
      populacao: lista com todos os indivíduos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """

    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_sv(individuo, senha_verdadeira, penalidade))
    
    return fitness


def mutacao_sv(individuo, letras, tamanho_max):
    """Realiza a mutação de um gene no problema da senha de tamanho variável
    Args:
      individuo: uma lista representado um indivíduo no problema da senha
      letras: letras possíveis de serem sorteadas
      tamanho_max: tamanho máximo para a senha
    Return:
      Um individuo (senha de tamanho n) com um gene e tamanho mutado.
    """
    # define aleatoriamente se a mutação no candidato irá ocorrer na letra ou no tamanho
    if random.random() < 0.5:
        gene =  random.randint(0, len(individuo) - 1)
        individuo[gene] = gene_sv(letras)
        return individuo    
    
    # define um novo tamanho possível cujo limite é o tamanho máximo
    else:
        novo_tamanho = random.randint(1, tamanho_max)    
        
        # corrige o tamanho do indivíduo caso ele seja maior que o novo tamanho
        if novo_tamanho < len(individuo):
            return individuo[:novo_tamanho]
        
        # corrige o tamanho do indivíduo caso ele seja menor que o tamanho
        else:
            for _ in range(novo_tamanho - len(individuo)):
                individuo.append(gene_sv(letras))
            return individuo


def cruzamento_ponto_simples_sv(pai, mae):
    """Operador de cruzamento de ponto simples.
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos.
    """

    # adaptação para o problema da senha de tamanho variável
    if len(pai) < len(mae):
        ponto_de_corte = random.randint(1, len(pai) - 1)
    else:
        ponto_de_corte = random.randint(1, len(mae) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2


def selecao_torneio_senha_sv(populacao, fitness, tamanho_torneio):
    """Faz a seleção de uma população usando torneio por meio de mimimização (seleção mimimi)
    Args:
        populacao: população do problema
        fitness: lista com os valores de fitness dos indivíduos da população
        tamanho_torneio: quantidade de indivíduos que batalham entre si
    Returns:
        selecionados: lista com os indivíduos selecionados com mesmo tamanho da população.
    """

    selecionados = []

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness))

    for _ in range(len(populacao)):
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio)

        # é assim que se escreve infinito em python
        melhor_fit = float('inf')

        for individuo, fit in combatentes:
            if fit < melhor_fit:
                selecionado = individuo
                melhor_fit = fit
        
        selecionados.append(selecionado)
    
    return selecionados