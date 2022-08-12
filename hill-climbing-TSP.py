from random import randrange
from tabnanny import verbose

class lista_circular:
    def __init__(self):
        self.lista   = []
        self.indice  = 0

    def add(self, e):
        self.lista.append(e)
    
    def __getitem__(self, idx):
        return self.lista[idx]

    def __setitem__(self, idx, val):
        self.lista[idx] = val

    def __len__(self):
        return len(self.lista)

    def acessar_proximo(self):
        e           = self.lista[self.indice]
        self.indice = (self.indice + 1) % len(self.lista)
        return e

# VARIÁVEL QUE REPRESENTA O NÚMERO DE VÉRTICES
n = 10

## ESSA LISTA GUARDA O GRAFO
list_adj = [[] for i in range(n)]

## GERA O GRAFO COMPLETO QUE SERÁ USADO NO HILL CLIMBING
for i in range(n):
    for j in range(i, n):
        if i != j:
            list_adj[i].append((j, randrange(3000)))
            list_adj[j].append((i, randrange(3000)))

## FUNÇÃO PRA DEBUG, SERVE PRA MOSTRAR O GRAFO COMPLETO
def printar_grafo():
    for i in range(n):
        print(i, list_adj[i])

# GERA O CAMINHO ALEATÓRIO INICIAL
def gerar_caminho_inicial():
    index    = [i for i in range(n)]
    vertices = lista_circular()

    # ESSA FUNÇÃO BASICAMENTE CRIA UM VETOR DE INDICES E EMBARALHA OS INDICES

    for i in range(n):
        ridx = randrange(n-i)
        vertices.add(index[ridx])
        index.remove(index[ridx])

    return vertices

# CALCULA O CUSTO DE UM DADO CAMINHO
def calcular_custo(vertices):
    custo = 0
    # APENAS SOMO O PESO DE CADA ARESTA E RETORNO NO FINAL
    for i in range(len(vertices)):
        custo = custo + list_adj[vertices[i]][[x for x in range(n-1) if list_adj[vertices[i]][x][0] == vertices[(i+1) % n]][0]][1]
    return custo

# FUNÇÃO PRA DEBUG, SERVE PRA PRINTAR UM DADO CAMINHO
def print_list(lista):
    for i in range(len(lista)):
        print(lista[i], end=' ')

# HILL CLIMBING EM QUESTÃO, IMPLEMENTADO DE ACORDO COM O PDF.. TROCANDO OS VIZINHOS, E CHECANDO SE HÁ ALGUM MELHOR QUE
# A MELHOR RESPOSTA ATUAL.. SE NÃO HOUVER, EU PARO.
def hill_climbing():
    vertices = gerar_caminho_inicial()

    # GUARDA O MELHOR ESTADO ATUAL
    melhor_estado = lista_circular()
    melhor_custo  = 100000000

    para_hill_climbing = 1
    while para_hill_climbing == 1:
        para_hill_climbing = 0
        # PRA CADA ITERAÇÃO AQUI EU GERO UM NOVO CAMINHO E VERIFICO SEU CUSTO
        for i in range(0, n-1, 2):
            vertices[i], vertices[i+1] = vertices[i+1], vertices[i]
        
            aux = calcular_custo(vertices)

            print("Custo apos uma troca: ", aux)

            if melhor_custo > aux:
                para_hill_climbing = 1 # ESSA VARIAVEL SERVE PARA VERIFICAR SE HOUVE ALGUMA MELHORIA NO RESULTADO APOS AS TROCAS
                melhor_custo  = aux
                melhor_estado = [vertices[x] for x in range(len(vertices))]
    
    # RETORNA O MELHOR CUSTO OBTIDO PELO ALGORITMO E O ESTADO DO CAMINHO CORRESPONDENTE
    return [melhor_custo, melhor_estado]

res = hill_climbing()

print("\nEstado final do caminho: ", end='')
print_list(res[1])

print('\n')

print("Menor caminho obtido: ", res[0])
