cap_shape = ['b', 'c', 'x', 'f', 'k', 's']
cap_surface = ['f', 'g', 'y', 's']
cap_color = ['n', 'b', 'c', 'g', 'r', 'p', 'u', 'e', 'w', 'y']
bruises = ['t', 'f']
odor = ['a', 'l', 'c', 'y', 'f', 'm', 'n', 'p', 's']
gill_attachment = ['a', 'd', 'f', 'n']
gill_spacing = ['c', 'w', 'd']
gill_size = ['b', 'n']
gill_color = ['k', 'n', 'b', 'h', 'g', 'r', 'o', 'p', 'u', 'e', 'w', 'y']
stalk_shape = ['e', 't']
stalk_root = ['b', 'c', 'u', 'e', 'z', 'r', '?']
stalk_surface_above_ring = ['f', 'y', 'k', 's']
stalk_surface_below_ring = ['f', 'y', 'k', 's']
stalk_color_above_ring = ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y']
stalk_color_below_ring = ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y']
veil_type = ['p', 'u']
veil_color = ['n', 'o', 'w', 'y']
ring_number = ['n', 'o', 't']
ring_type = ['c', 'e', 'f', 'l', 'n', 'p', 's', 'z']
spore_print_color = ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y']
population = ['a', 'c', 'n', 's', 'v', 'y']
habitat = ['g', 'l', 'm', 'p', 'u', 'w', 'd']

nomes_atr = [cap_shape, cap_surface, cap_color, bruises, odor, gill_attachment, gill_spacing, gill_size, gill_color, stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring, stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type, spore_print_color, population, habitat]

Xtrain = []
Xtrain_num = []
Ytrain = []
Xtest = []
Xtest_num =[]
Xtest_num_trans = []
cogu_numerado_teste = []
cogu_numerado_treino = []
atributos_numerados = []
desvios = []
medias = []
somatorio = int()
Xtrain_num_normalizada = []

for tipo_atributo in nomes_atr: #Faz uma nova lista com os valores de cada atributo.
    tipo_atributo_num = list(zip(tipo_atributo, range(len(tipo_atributo))))
    mapeada = []
    for _, n in tipo_atributo_num:
        mapeada.append(n)
    atributos_numerados.append(mapeada)

K = int(input())
Ntrain, Ntest = map(int, input().split())

for i in range(Ntrain):        #Recebe a lista de cogumelos de treino
    car_cogu = input().split()
    Xtrain.append(car_cogu)

for i in Xtrain:       #Transforma a lista em seus respectivos números
    cogu_numerado_treino = [cap_shape.index(i[0]), cap_surface.index(i[1]), cap_color.index(i[2]), bruises.index(i[3]), odor.index(i[4]), gill_attachment.index(i[5]), gill_spacing.index(i[6]), gill_size.index(i[7]), gill_color.index(i[8]), stalk_shape.index(i[9]), stalk_root.index(i[10]), stalk_surface_above_ring.index(i[11]), stalk_surface_below_ring.index(i[12]), stalk_color_above_ring.index(i[13]), stalk_color_below_ring.index(i[14]), veil_type.index(i[15]), veil_color.index(i[16]), ring_number.index(i[17]), ring_type.index(i[18]), spore_print_color.index(i[19]), population.index(i[20]), habitat.index(i[21])]
    Xtrain_num.append(cogu_numerado_treino)

Xtrain_num_trans = list(map(list, zip(*Xtrain_num)))  #Transpõe o conjunto de treino

for i in Xtrain_num_trans: #tira a média de cada atributo de treino
    media = sum(i)/len(i)
    medias.append(media)

for j in range(22): # Tira os desvios padrões de cada atributo de treino
    somatorio = 0
    for i in range(Ntrain):
        somatorio += (Xtrain_num[i][j] - medias[j])**2
    vetor_desvio = (1/Ntrain * somatorio)**(1/2)
    desvios.append(vetor_desvio)

for i in range(Ntrain):       #Recebe os rótulos de cada cogumelow
    rotulo = input()
    Ytrain.append(list(rotulo))

for i in range(Ntest):        #Recebe o conjunto de teste
    car_cogu = input().split()
    Xtest.append(car_cogu)

for i in Xtest:       #Transforma a lista em seus respectivos números
    cogu_numerado_teste = [cap_shape.index(i[0]), cap_surface.index(i[1]), cap_color.index(i[2]), bruises.index(i[3]), odor.index(i[4]), gill_attachment.index(i[5]), gill_spacing.index(i[6]), gill_size.index(i[7]), gill_color.index(i[8]), stalk_shape.index(i[9]), stalk_root.index(i[10]), stalk_surface_above_ring.index(i[11]), stalk_surface_below_ring.index(i[12]), stalk_color_above_ring.index(i[13]), stalk_color_below_ring.index(i[14]), veil_type.index(i[15]), veil_color.index(i[16]), ring_number.index(i[17]), ring_type.index(i[18]), spore_print_color.index(i[19]), population.index(i[20]), habitat.index(i[21])]
    Xtest_num.append(cogu_numerado_teste)

Xtest_num_trans = list(map(list, zip(*Xtest_num)))  #Transpõe o conjunto de teste

k = 0
vetor_norm = []
vetores_treino_normalizados = []

while True:       #Normaliza os vetores do conjunto de treino de acordo com os pesos dados.
    for i in Xtrain_num_trans[k]:
        if desvios[k] != 0:
            val = (i- medias[k])/desvios[k]
        else:
            val = 0
        vetor_norm.append(val)
    vetores_treino_normalizados.append(list(vetor_norm))
    vetor_norm = []
    k += 1
    if k == 22:
        break
vetores_treino_normalizados = list(map(list, zip(*vetores_treino_normalizados))) #transpõe a normalizada para recuperar pesos de cada um dos casos de treino

const = 0

vetores_teste_normalizados = []

while True:       #Normaliza os vetores do conjunto de teste de acordo com os pesos dados.
    for i in Xtest_num_trans[const]:
        if desvios[const] != 0:
            val = (i- medias[const])/desvios[const]
        else:
            val = 0
        vetor_norm.append(val)
    vetores_teste_normalizados.append(list(vetor_norm))
    vetor_norm = []
    const += 1
    if const == 22:
        break
vetores_teste_normalizados = list(map(list, zip(*vetores_teste_normalizados)))

distancias = []

for vetor_teste in vetores_teste_normalizados:    #A distância entre dois vetores é o somatório do quadrado da diferença
    distancias_teste = []
    for vetor_treino in vetores_treino_normalizados:  #distancia_teste armazena as distancias entre o vetor distancia_teste[i] e os vetores distancia_treino[j]
        soma = 0
        for j in range(22):
            soma += (vetor_teste[j] - vetor_treino[j])**2
        distancia = (soma)**(1/2)
        distancias_teste.append(distancia)
    distancias.append(distancias_teste)



indices = []

for distancia_vetor in distancias:
    Kmenores = []
    marcados = [False] * len(distancia_vetor)  # Inicializa a lista de marcadores como False
    
    for _ in range(K):
        menor_valor = float('inf')
        indice_menor = -1
        
        # Encontra o menor valor que ainda não foi marcado
        for i, valor in enumerate(distancia_vetor):
            if not marcados[i] and valor < menor_valor:
                menor_valor = valor
                indice_menor = i
        
        # Marca o índice do menor valor encontrado
        marcados[indice_menor] = True
        Kmenores.append(indice_menor)
    
    indices.append(Kmenores)

safado = []

for cogupertos in indices:
    comer = []
    for i in cogupertos:
        comer.append(Ytrain[i][0])  # Adiciona o primeiro (e único) elemento do rótulo
    safado.append(comer)

for i in safado:
    countp = i.count('p')
    counte = i.count('e')
    if countp > counte:
        print('p')
    else:
        print('e')