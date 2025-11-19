import random
# Aqui e onde a gente arruma os Parametros do Algoritmo Genetico
# Podemos alterar esses valores para ver como afetam o desempenho do algoritmo
POPULACAO_SIZE = 200    # Aqui fazemos o set do tamanho da populacao, ou seja: O numero de individuos (posicoes no texto) por geracao
NUM_GERACOES   = 100    # Aqui o set é do numero de geracoes, representando quantas vezes a populacao vai evoluir
TAXA_MUTACAO   = 0.2    # E por fim a taxa de mutacao, que determinamos a probabilidade de mutacao em um cromossomo (Como tratamos em percentual, o 0.2 equivale a 20%)

# Aqui comeca o calculo da similaridade entre o trecho do texto e o padrao escolhido.
def calc_padrao(posicao, padrao, texto): # Funcao Fitness
    # Retorna a proporcao de caracteres identicos entre o padrao e o trecho do texto iniciado em 'posicao'.
    trecho = texto[posicao: posicao + len(padrao)]
    # Se o trecho for menor que o padrao (o que de regra não pode acontecer), retorna 0 de similaridade
    if len(trecho) < len(padrao):
        return 0.0
    # Conta quantos caracteres coincidem nas posicoes correspondentes
    coincidencias = 0
    for i, char in enumerate(padrao):
        if trecho[i] == char:
            coincidencias += 1
    # Similaridade em percentual (0.0 a 1.0)
    return coincidencias / len(padrao)

# Pegamos o metodo de selecao de torneio
def selecionar_pai_torneio(populacao, aptidoes, k=3):
    # Seleciona um individuo da populacao com modo de torneio.
    # Escolhe 'k' indices aleatorios da populacao e retorna o individuo de maior aptidao.
    # Seleciona k individuos aleatoriamente
    candidatos = random.sample(range(len(populacao)), k)
    melhor = candidatos[0]
    for indice in candidatos[1:]:
        if aptidoes[indice] > aptidoes[melhor]:
            melhor = indice
    return populacao[melhor]

# Operador de crossover
def crossover_um_ponto(pai1, pai2, max_index):
    # Realiza crossover de um ponto entre dois pais (que seriam posicoes).
    # Representa os indices em binario e combina as partes de cada um.
    if max_index <= 0:
        return 0  # Casos comuns onde o texto e menor ou igual ao tamanho do padrao
    # Define o comprimento em bits necessario para representar o maior indice
    bits = max_index.bit_length()
    # Escolhe aleatoriamente um ponto de corte (entre 1 e bits-1)
    corte = random.randint(1, bits - 1)
    # Mascara de bits para separar a esquerda e a direita do ponto de corte
    mascara_inferior = (1 << corte) - 1    # bits inferiores (direita)
    mascara_superior = ((1 << bits) - 1) ^ mascara_inferior  # bits superiores (esquerda)
    # Combina bits dos pais conforme as mascaras
    filho = (pai1 & mascara_superior) | (pai2 & mascara_inferior)
    # Garante que o resultado esteja dentro dos limites [0, max_index]
    if filho > max_index:
        filho = filho % (max_index + 1)
    return filho

# Funcao do operador de mutacao
def mutacao(cromossomo, max_index, taxa_mutacao):
    # Aplica mutacao ao cromossomo (que e a posicao) com a probabilidade recebida.
    # A mutacao consiste em substituir por uma nova posicao aleatoria valida.
    if random.random() < taxa_mutacao:
        return random.randint(0, max_index)
    return cromossomo

# Essa e a funcao com o AG principal. Focado em evoluir a populacao e retornar o melhor resultado
def algoritmo_genetico(texto, padrao, tamanho_pop=POPULACAO_SIZE, geracoes=NUM_GERACOES, taxa_mut=TAXA_MUTACAO):
    # Determina o indice maximo inicial (que seria a ultima posicao inicial possivel para o padrao no texto)
    max_index = len(texto) - len(padrao)
    if max_index < 0:
        raise ValueError("O padrao e maior do que o texto fornecido.")
    # Geracao inicial da populacao com posicoes aleatorias no texto
    populacao = [random.randint(0, max_index) for _ in range(tamanho_pop)]
    melhor_individuo = None # melhor posicao encontrada
    melhor_aptidao = 0.0 # melhor aptidao (similaridade) encontrada

    # Loop evolutivo atraves das geracoes
    for gen in range(geracoes):
        # Calcula aptidao de cada individuo da populacao
        aptidoes = [calc_padrao(pos, padrao, texto) for pos in populacao]
        # Verifica o melhor individuo da geracao atual
        for pos, apt in zip(populacao, aptidoes):
            if apt > melhor_aptidao:
                melhor_aptidao = apt
                melhor_individuo = pos
        # Se atingiu 100% de similaridade, pode encerrar antes (porque isso significa que o padrao exato foi encontrado no texto)
        if melhor_aptidao == 1.0:
            break

        # Nova populacao a ser gerada via selecao, crossover e mutacao
        nova_populacao = []
        while len(nova_populacao) < tamanho_pop:
            # Selecao dos pais via torneio
            pai1 = selecionar_pai_torneio(populacao, aptidoes)
            pai2 = selecionar_pai_torneio(populacao, aptidoes)
            # Crossover de um ponto entre pai1 e pai2 para gerar um filho
            filho = crossover_um_ponto(pai1, pai2, max_index)
            # Mutacao do filho gerado
            filho = mutacao(filho, max_index, taxa_mut)
            # Adiciona o novo individuo na nova populacao
            nova_populacao.append(filho)
        # Substitui a populacao antiga pela nova
        populacao = nova_populacao

    # Retorna a melhor solucao encontrada (posicao no texto) e a aptidao (similaridade entre padrao e trecho correspondente)
    return melhor_individuo, melhor_aptidao

if __name__ == "__main__":
    # Leitura do texto completo de "dom_casmurro.txt" (aqui ele vai considerar encoding UTF-8 por causa da acentuacao)
    with open("dom_casmurro.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    # Le o padrao de busca fornecido pelo usuario
    padrao = input("Digite o padrao de busca: ")
    # Executa o algoritmo genetico com parametros definidos
    posicao, sim = algoritmo_genetico(texto, padrao)
    # Prepara o trecho encontrado (subtexto) para exibir
    trecho_encontrado = texto[posicao: posicao + len(padrao)]
    # Exibe o resultado de posicao, trecho correspondente e porcentagem de similaridade
    porcentagem = sim * 100
    print(f"Melhor posicao encontrada: {posicao}")
    print(f"Trecho correspondente: \"{trecho_encontrado}\"")
    print(f"Similaridade: {porcentagem:.2f}%")
