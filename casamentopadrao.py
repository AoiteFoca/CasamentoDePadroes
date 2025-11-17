import random
POPULACAO_SIZE = 200
NUM_GERACOES   = 100
TAXA_MUTACAO   = 0.2

def calcular_fitness(posicao, padrao, texto):
    trecho = texto[posicao: posicao + len(padrao)]
    if len(trecho) < len(padrao):
        return 0.0
    coincidencias = 0
    for i, char in enumerate(padrao):
        if trecho[i] == char:
            coincidencias += 1
    return coincidencias / len(padrao)

def selecionar_pai_torneio(populacao, aptidoes, k=3):
    candidatos = random.sample(range(len(populacao)), k)
    melhor = candidatos[0]
    for indice in candidatos[1:]:
        if aptidoes[indice] > aptidoes[melhor]:
            melhor = indice
    return populacao[melhor]

def crossover_um_ponto(pai1, pai2, max_index):
    if max_index <= 0:
        return 0
    bits = max_index.bit_length()
    corte = random.randint(1, bits - 1)
    mascara_inferior = (1 << corte) - 1
    mascara_superior = ((1 << bits) - 1) ^ mascara_inferior
    filho = (pai1 & mascara_superior) | (pai2 & mascara_inferior)
    if filho > max_index:
        filho = filho % (max_index + 1)
    return filho

def mutacao(cromossomo, max_index, taxa_mutacao):
    if random.random() < taxa_mutacao:
        return random.randint(0, max_index)
    return cromossomo

def algoritmo_genetico(texto, padrao, tamanho_pop=POPULACAO_SIZE, geracoes=NUM_GERACOES, taxa_mut=TAXA_MUTACAO):
    max_index = len(texto) - len(padrao)
    if max_index < 0:
        raise ValueError("O padrao e maior do que o texto fornecido.")
    populacao = [random.randint(0, max_index) for _ in range(tamanho_pop)]
    melhor_individuo = None
    melhor_aptidao = 0.0

    for gen in range(geracoes):
        aptidoes = [calcular_fitness(pos, padrao, texto) for pos in populacao]
        for pos, apt in zip(populacao, aptidoes):
            if apt > melhor_aptidao:
                melhor_aptidao = apt
                melhor_individuo = pos
        if melhor_aptidao == 1.0:
            break

        nova_populacao = []
        while len(nova_populacao) < tamanho_pop:
            pai1 = selecionar_pai_torneio(populacao, aptidoes)
            pai2 = selecionar_pai_torneio(populacao, aptidoes)
            filho = crossover_um_ponto(pai1, pai2, max_index)
            filho = mutacao(filho, max_index, taxa_mut)
            nova_populacao.append(filho)
        populacao = nova_populacao

    return melhor_individuo, melhor_aptidao

if __name__ == "__main__":
    with open("dom_casmurro.txt", "r", encoding="utf-8") as f:
        texto = f.read()
    padrao = input("Digite o padrao de busca: ")
    posicao, sim = algoritmo_genetico(texto, padrao)
    trecho_encontrado = texto[posicao: posicao + len(padrao)]
    porcentagem = sim * 100
    print(f"Melhor posicao encontrada: {posicao}")
    print(f"Trecho correspondente: \"{trecho_encontrado}\"")
    print(f"Similaridade: {porcentagem:.2f}%")