import numpy as np
from random import randint
# TODO: Buscar un metodo el cual permita generar matrices aleatorias
#mt_base = [[5,6,1],[2,3,4],[1,2,7]]
#mt_base_inv = np.linalg.inv(mt_base)

# Recibe rango de inicio y final del rango. Retorna una matriz aleatoria en base si esta posee un inverso 
def generar_matriz_aleatoria(RangoInicio=0,RangoFinal=50):
    while True:
        # CHECK: Es esta una forma correcta de usar try's?
        try:
            matriz = np.empty((3,3))
            for x in range(3):
                for y in range(3):
                    matriz[x][y] = randint(RangoInicio,RangoFinal)
            matriz_inv = np.linalg.inv(matriz)
        except np.linalg.LinAlgError as err:
            if 'Singular matrix' in str(err):
                continue
        else:
            return matriz


# Recibe una cadena cuyos caracteres son convertidos a Unicode y pasados a una matriz nx3. Retorna numpy.narray(dtype=int64)
def convertir_a_matriz(cadena):
    matriz_final = np.empty((int(len(cadena)/3), 3))
    matriz_final = matriz_final.astype('int64')
    comp = 0
    y = 0
    for x in range(len(cadena)):
        matriz_final[comp][y] = ord(cadena[x])
        y += 1
        if y > 2:
            comp+=1     
            y = 0    
    return matriz_final

# Recibe una matriz, los valores almacenados son convertidos de Unicode a texto plano. Retorna un string
def convertir_a_texto(matriz):
    texto = ""
    for y_mt in range(len(matriz)):
        for x_mt in range(3):
            # TODO: Remover esta parte y comprobar que no haya problemas
            if(matriz[y_mt][x_mt] < 0):
                texto += chr(int(matriz[y_mt][x_mt])*-1)
                continue
            texto += chr(int(matriz[y_mt][x_mt]))
    return texto

# Recibe dos matrices, una matriz de cadenas y una matriz llave. Esta funcion multiplica ambas matrices. Retorna un numpy.narray(dtype=int64)
def codificador(matriz_cadena, matriz_codificador):
    mt_str_cod = np.empty((len(matriz_cadena),3))
    mt_str_cod = mt_str_cod.astype('int64')
    temp = 0
    # TODO: Buscar un mejor metodo que no requiera 3 for's
    for i in range(len(matriz_cadena)):
        for x_mt_cod in range(3):
            for x_mt_str in range(3):
                temp += matriz_cadena[i][x_mt_str] * matriz_codificador[x_mt_cod][x_mt_str]
                if x_mt_str == 2:
                    mt_str_cod[i][x_mt_cod] = round(temp)
                    temp = 0
    return mt_str_cod

#print(generar_matriz_aleatoria(0,256))
mt_base = generar_matriz_aleatoria(0,128)
mt_base_inv = np.linalg.inv(mt_base)
texto = "uno"
print("Matriz llave:\n",mt_base)
print("Matriz inv:\n",mt_base_inv)
texto_matriz = convertir_a_matriz(texto)
print("Matriz sin encriptar:\n", texto_matriz)
print(convertir_a_texto(texto_matriz))
texto_matriz_cifrado = codificador(texto_matriz,mt_base)
print("Matriz cifrada:\n", texto_matriz_cifrado)
print(convertir_a_texto(texto_matriz_cifrado))
texto_matriz_decifrado = codificador(texto_matriz_cifrado, mt_base_inv)
print("Matriz decifrada:\n", texto_matriz_decifrado)
print(convertir_a_texto(texto_matriz_decifrado))