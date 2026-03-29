#distancia angular do equador e meridiano de greenwich.
#Coordenadas são dadas pelo vetor (x,y,z)
import numpy as np
print(np.__version__)

#A - Faca uma funcao que receba as coordenadas e retorne o vetor posicao correspondente.
# Teste nas seguintes cidades:
def vet_posi(Lati,Longi):
    R = 6367.5
    Lati = np.radians(Lati)
    Longi = np.radians(Longi)
    
    x = R*np.cos(Longi)*np.sin(Lati)
    y = R*np.cos(Longi)*np.cos(Lati)
    z = R*np.sin(Longi)
    
    return np.array((x,y,x))

SP = vet_posi(-23.5505,-46.6333)
Londres = vet_posi(51.5074,-0.1278)
Sydney = vet_posi(-33.8688,151.2093)
Toquio = vet_posi(35.6895,139.6917)
NY = vet_posi(40.7128,-46.6333)

print("\n",SP, Londres)

#B - Calcule as distancias euclidianas em 3D entre S ̃ao Paulo e as outras cidades utilizando o
# vetor posiçao.

def calc_dist(vet_cidade1,vet_cidade2):
    dist = np.linalg.norm(vet_cidade1 - vet_cidade2)
    return dist

distan = [
    calc_dist(SP,NY), 
    calc_dist(SP,Toquio), 
    calc_dist(SP,Sydney),
    calc_dist(SP,Londres)
]
print("\nDistancias: ")
for dist in distan:
    print(dist)


#C - Faça uma função que calcule a distância na superfície da Terra entre dois pontos dadas 
#suas coordenadas. Utilize a f ́ormula d(a, b) = R∠(a, b) e teste no mesmo caso do exercício
# anterior.

def dist_superficie(vet1,vet2):
    R = 6367.5
    dist_Terra = R*calc_dist(vet1,vet2)
    return dist_Terra

distan_ST = [
    dist_superficie(SP,NY),
    dist_superficie(SP,Toquio),
    dist_superficie(SP,Sydney),    
    dist_superficie(SP,Londres)
]
print("\nDistância superficie da Terra: ")
for d in distan_ST:
    print(d)


#Exercício 2

#A - Compare a semelhan ̧ca entre o Brasil e outros pa ́ıses utilizando a distˆancia euclidiana entre
# os vetores de caracter ́ısticas (PIB, Popula ̧c ̃ao, Infla ̧c ̃ao, Desemprego).
tabela = np.array([
    [2.1, 213, 3.2,11.2],
    [21.4,331,2.1,3.7],
    [14.3,1439,2.9,3.8],
    [3.8,83,1.4,3.2],
    [4.9,126,0.5,2.8],
    [2.6,67,1.8,8.1],
    [2.8,67,2.5,4.1],
    [1.7,38,1.9,5.7]
])
def dist_euclid(table):
    dist = []

    for i in range(table.shape[0]):
        distancia = np.linalg.norm(table[0]-table[i])
        dist.append(float(distancia))
        
    return dist
d = dist_euclid(tabela)
print("\n")
print(d)

#B - Fa ̧ca a padroniza ̧c ̃ao dos dados utilizando a t ́ecnica de z-score em cada uma das carac-
# ter ́ısticas. Ap ́os a padroniza ̧c ̃ao, compare novamente a semelhan ̧ca entre os pa ́ıses. Explique
# a diferen ̧ca nos resultados comparados com o item anterior.

def padroniz(table):
    mean_col = np.mean(table)
    std_col = np.std(table)
    z = (table - mean_col)/std_col

    return z


matriz_z = np.zeros_like(tabela,dtype=float)
for i in range(tabela.shape[1]):
    matriz_z[:,i] = padroniz(tabela[:,i])
    
print(matriz_z)


#C - Compute a matriz de correlacao entre os países.

tabela_med = np.mean(tabela,axis=1, keepdims=True)
tabela_centrada = tabela - tabela_med
corr = np.zeros((tabela.shape[0],tabela.shape[0]))

for i in range(tabela.shape[0]):
    vi = tabela_centrada[i,:]
    for j in range(i,tabela.shape[0]):
        vj = tabela_centrada[j,:]
        c = np.dot(vi,vj)/(np.linalg.norm(vi)*np.linalg.norm(vj))

        corr[i,j] = c
        corr[j,i] = c                        
print(np.round(corr, 4))           

#com z
for i in range(tabela.shape[0]):
    vi = matriz_z[i,:]
    for j in range(i,tabela.shape[0]):
        vj = matriz_z[j,:]
        c = np.dot(vi,vj)/(np.linalg.norm(vi)*np.linalg.norm(vj))

        corr[i,j] = c
        corr[j,i] = c   
print(np.round(corr, 4))  