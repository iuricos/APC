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

# f s g t f f c b w t b f s w w p w o p h v g

K =  int(input())
Ntrain, Ntest = map(int, input().split())

Xtrain = []
Xtrain_num = []
cogu_numerado = []
atributos_numerados = []
bagulho = int()


for i in range(Ntrain):
    car_cogu = input().split()
    Xtrain.append(car_cogu)

for i in Xtrain:
    cogu_numerado = [cap_shape.index(i[0]), cap_surface.index(i[1]), cap_color.index(i[2]), bruises.index(i[3]), odor.index(i[4]), gill_attachment.index(i[5]), gill_spacing.index(i[6]), gill_size.index(i[7]), gill_color.index(i[8]), stalk_shape.index(i[9]), stalk_root.index(i[10]), stalk_surface_above_ring.index(i[11]), stalk_surface_below_ring.index(i[12]), stalk_color_above_ring.index(i[13]), stalk_color_below_ring.index(i[14]), veil_type.index(i[15]), veil_color.index(i[16]), ring_number.index(i[17]), ring_type.index(i[18]), spore_print_color.index(i[19]), population.index(i[20]), habitat.index(i[21])]
    Xtrain_num.append(cogu_numerado)

for tipo_atributo in nomes_atr:
    tipo_atributo_num = list(zip(tipo_atributo, range(len(tipo_atributo))))
    mapeada = []
    for _, n in tipo_atributo_num:
        mapeada.append(n)
    atributos_numerados.append(mapeada)


medias = []

for atributo in atributos_numerados:
    media = sum(atributo)/len(atributo)
    medias.append(media)
    i = 1

    while i != Ntrain:
        bagulho += (atributo[i]- media[i])**2
    
    desvio = (bagulho/Ntrain)**(1/2)
    print(desvio)

