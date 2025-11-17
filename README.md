<p align="center">
    <img loading="lazy" src="https://files.engaged.com.br/5db0810e95b4f900077e887e/account/5db0810e95b4f900077e887e/xMCS8NFKTMqwhefy8WLd_catolica-horizontal.png" width="300">
</p>

## Situação do Projeto
![Status](https://img.shields.io/badge/Status-Em%20Andamento-blue)

![Etapa](https://img.shields.io/badge/Etapa-N3-green)

# Casamento De Padrões

Este projeto implementa um **Algoritmo Genético (AG)** para realizar **casamento de padrões aproximado** dentro de um texto extenso.  
O objetivo é localizar, no arquivo `dom_casmurro.txt`, o trecho mais semelhante a um padrão informado pelo usuário, mesmo que não haja correspondência exata.

A técnica aplicada tolera:
- Substituições;
- Erros de digitação;
- Acentos;
- Caracteres especiais.

O algoritmo retorna:
- A **melhor posição encontrada**;  
- O **trecho correspondente**;  
- A **similaridade percentual**.

---

## Estratégia Evolutiva Utilizada

### Representação dos Indivíduos
- Cada indivíduo é uma **posição inicial** dentro do texto;
- A população contém várias posições diferentes;
- A evolução busca regiões do texto onde o padrão se encaixa melhor.

---

## Componentes do Algoritmo

### **1. População**
```python
POPULACAO_SIZE = 200
```
Escolhido para balancear diversidade e desempenho.

---

### **2. Número de Gerações**
```python
NUM_GERACOES = 100
```
Suficiente para convergência em testes empíricos.

---

### **3. Taxa de Mutação**
```python
TAXA_MUTACAO = 0.2
```
Mutação alta ajuda a explorar regiões distantes do texto.

---

### **4. Função de Fitness**
Compara caractere a caractere:
```python
coincidencias / len(padrao)
```
Simples, eficiente e adequado ao problema de similaridade direta.

---

### **5. Seleção por Torneio**
```python
selecionar_pai_torneio(pop, aptidoes, k=3)
```
Robusta, simples e garante pressão seletiva balanceada.

---

### **6. Crossover de Um Ponto**
Realizado na forma binária das posições:
```python
corte = random.randint(1, bits - 1)
```
Combina trechos dos pais para formar nova posição.

---

### **7. Mutação**
A mutação redefine completamente a posição:
```python
random.randint(0, max_index)
```

---

### **8. Critério de Parada**
- Encontrar similaridade **100%**, ou  
- Completar todas as gerações.

---

## Arquivos do Projeto

```
raiz do projeto/
 ├── dom_casmurro.txt
 ├── casamentopadrao.py
 ├── README.md
 └── report.md
```

---

## Como Executar

1. Coloque todos os arquivos no Replit ou no seu ambiente local.
2. Rode `casamentopadrao.py`.
3. Digite o padrão desejado:
```
Digite o padrão de busca: A casa em que moro é própria
```
4. Resultado esperado:
```
Melhor posição encontrada: 12345
Trecho correspondente: " casa em que moro é própria!"
Similaridade: 96.43%
```

---

## Limitações

- Mutação completamente aleatória pode atrasar ajustes finos;
- Falta elitismo: indivíduos bons podem ser perdidos;
- Similaridade baseada apenas em posição exata dos caracteres.

---

## Conclusão

Este projeto demonstra como Algoritmos Genéticos são adequados para problemas de busca aproximada em textos.  
Mesmo com uma implementação simples, o método obtém altas taxas de similaridade (>85%) com eficiência.

---

## Contribuidores

A equipe envolvida nesta atividade é constituída por alunos da 7ª Fase (20252) do curso de Engenharia de Software do Centro Universitário Católica SC de Jaraguá do Sul.

<div align="center">
<table>
  <tr>
    <td align="center"><a href="https://github.com/HigorAz"><img loading="lazy" src="https://avatars.githubusercontent.com/u/141787745?v=4" width="115"><br><sub>Higor Azevedo</sub></a></td>
    <td align="center"><a href="https://github.com/AoiteFoca"><img loading="lazy" src="https://avatars.githubusercontent.com/u/141975272?v=4" width="115"><br><sub>Nathan Cielusinski</sub></a></td>
    <td align="center"><a href="https://github.com/MrNicolass"><img loading="lazy" src="https://avatars.githubusercontent.com/u/80847876?v=4" width="115"><br><sub>Nicolas Gustavo 
  </tr>
</div>

