import re

# Definición de las tablas de símbolos
palabras_reservadas = {
    'SELECT': ('s', 10),
    'FROM': ('f', 11),
    'WHERE': ('w', 12),
    'IN': ('n', 13),
    'AND': ('y', 14),
    'OR': ('o', 15),
    'CREATE': ('c', 16),
    'TABLE': ('t', 17),
    'CHAR': ('h', 18),
    'NUMERIC': ('u', 19),
    'NOT': ('e', 20),
    'NULL': ('g', 21),
    'CONSTRAINT': ('b', 22),
    'KEY': ('k', 23),
    'PRIMARY': ('p', 24),
    'FOREIGN': ('j', 25),
    'REFERENCES': ('l', 26),
    'INSERT': ('m', 27),
    'INTO': ('q', 28),
    'VALUES': ('v', 29)
}

delimitadores = {
    ',': ('DELIMITADOR', 50),
    '.': ('DELIMITADOR', 51),
    '(': ('DELIMITADOR', 52),
    ')': ('DELIMITADOR', 53),
    '‘': ('DELIMITADOR', 54),
    "'": ('DELIMITADOR', 54),  
     
}

operadores = {
    '+': ('OPERADOR', 70),
    '-': ('OPERADOR', 71),
    '*': ('OPERADOR', 72),
    '/': ('OPERADOR', 73)
}

constantes = {}

relacionales = {
    '>': ('RELACIONAL', 81),
    '<': ('RELACIONAL', 82),
    '=': ('RELACIONAL', 83),
    '>=': ('RELACIONAL', 84),
    '<=': ('RELACIONAL', 85)
}
primeros_ts = {
    300: 10,
    301: 302,
    302: 304,
    303: 50,
    304: 4,
    305: 51,
    306: 308,
    307: 50,
    308: 4,
    309: 4,
    310: 12,
    311: 313,
    312: 317,
    313: 304,
    314: 315,
    315: 8,
    316: 304,
    317: 14,
    318: 62,
    319: 61
}

# Suponiendo que tienes diccionarios como los siguientes:
indices_estados = {300: 0, 301: 1, 302: 2, 303: 3, 304: 4, 305: 5, 306: 6, 307: 7, 308: 8, 309: 9, 310: 10, 311: 11, 312: 12, 313: 13, 314: 14 , 315: 15, 316: 16, 317: 17, 318: 18, 319: 19,}  # etc...
indices_tokens = {4: 0, 8: 1, 10: 2, 11: 3, 12: 4, 13: 5, 14: 6, 15: 7, 50: 8, 51: 9, 53: 10, 54: 11, 61: 12, 62: 13, 72: 14, 199: 15}  # etc...

# Inicializar la tabla sintáctica con listas vacías o None
tabla_sintactica = [[None for _ in range(len(indices_tokens))] for _ in range(len(indices_estados))]

# Llenar las filas según los estados y tokens
tabla_sintactica[indices_estados[300]][indices_tokens[10]] = [10,301,11,306,310]
tabla_sintactica[indices_estados[301]][indices_tokens[4]] = [302]
tabla_sintactica[indices_estados[301]][indices_tokens[72]] = [72]
tabla_sintactica[indices_estados[302]][indices_tokens[4]] = [304, 303]
tabla_sintactica[indices_estados[303]][indices_tokens[11]] = [99]
tabla_sintactica[indices_estados[303]][indices_tokens[50]] = [50, 302]
tabla_sintactica[indices_estados[303]][indices_tokens[199]] = [99]
tabla_sintactica[indices_estados[304]][indices_tokens[4]] = [4, 305]
tabla_sintactica[indices_estados[305]][indices_tokens[8]] = [99]
tabla_sintactica[indices_estados[305]][indices_tokens[11]] = [99]
tabla_sintactica[indices_estados[305]][indices_tokens[13]] = [99]
tabla_sintactica[indices_estados[305]][indices_tokens[14]] = [99]
tabla_sintactica[indices_estados[305]][indices_tokens[15]] = [99]
tabla_sintactica[indices_estados[305]][indices_tokens[50]] = [99]
tabla_sintactica[indices_estados[305]][indices_tokens[51]] = [51, 4]
tabla_sintactica[indices_estados[305]][indices_tokens[53]] = [99]
tabla_sintactica[indices_estados[305]][indices_tokens[199]] = [99]
tabla_sintactica[indices_estados[306]][indices_tokens[4]] = [308, 307]
tabla_sintactica[indices_estados[307]][indices_tokens[12]] = [99]
tabla_sintactica[indices_estados[307]][indices_tokens[50]] = [50, 306]
tabla_sintactica[indices_estados[307]][indices_tokens[53]] = [99]
tabla_sintactica[indices_estados[307]][indices_tokens[199]] = [99]
tabla_sintactica[indices_estados[308]][indices_tokens[4]] = [4, 309]
tabla_sintactica[indices_estados[309]][indices_tokens[4]] = [4]
tabla_sintactica[indices_estados[309]][indices_tokens[12]] = [99]
tabla_sintactica[indices_estados[309]][indices_tokens[50]] = [99]
tabla_sintactica[indices_estados[309]][indices_tokens[53]] = [99]
tabla_sintactica[indices_estados[309]][indices_tokens[199]] = [99]
tabla_sintactica[indices_estados[310]][indices_tokens[12]] = [12, 311]
tabla_sintactica[indices_estados[310]][indices_tokens[53]] = [99]
tabla_sintactica[indices_estados[310]][indices_tokens[199]] = [99]
tabla_sintactica[indices_estados[311]][indices_tokens[4]] = [313, 312]
tabla_sintactica[indices_estados[312]][indices_tokens[14]] = [317, 311]
tabla_sintactica[indices_estados[312]][indices_tokens[15]] = [317, 311]
tabla_sintactica[indices_estados[312]][indices_tokens[53]] = [99]
tabla_sintactica[indices_estados[312]][indices_tokens[199]] = [99]
tabla_sintactica[indices_estados[313]][indices_tokens[4]] = [304, 314]
tabla_sintactica[indices_estados[314]][indices_tokens[8]] = [315, 316]
tabla_sintactica[indices_estados[314]][indices_tokens[13]] = [13, 52, 300, 53]
tabla_sintactica[indices_estados[315]][indices_tokens[8]] = [8]
tabla_sintactica[indices_estados[316]][indices_tokens[4]] = [304]
tabla_sintactica[indices_estados[316]][indices_tokens[54]] = [54, 318, 54]
tabla_sintactica[indices_estados[316]][indices_tokens[61]] = [319]
tabla_sintactica[indices_estados[317]][indices_tokens[14]] = [14]
tabla_sintactica[indices_estados[317]][indices_tokens[15]] = [15]
tabla_sintactica[indices_estados[318]][indices_tokens[62]] = [62]
tabla_sintactica[indices_estados[319]][indices_tokens[61]] = [61]


# Códigos de errores léxicos y sintácticos
# errores = {
#     101: ("Símbolo desconocido", 1),
#     200: ("Sin error",2),
#     201: ("Se esperaba Palabra Reservada", 2),
#     204: ("Se esperaba Identificador", 2),
#     205: ("Se esperaba Delimitador", 2),
#     206: ("Se esperaba Constante", 2),
#     207: ("Se esperaba Operador", 2),
#     208: ("Se esperaba Operador Relacional", 2)
# }

def escanear_entrada(entrada):
    lineas = entrada.split('\n')
    tabla_lexica = []
    tabla_identificadores = {}
    tabla_constantes = {}
    errores = []
    codigos_tokens = []  # Lista para almacenar los códigos de tokens, incluyendo los errores
    lineas_tokens=[]
    num_linea = 1
    num_identificador = 401
    num_constante = 600
    
    for linea in lineas:
        tokens = re.findall(r"[,.()]|[-+*/]|>=?|<=?|[><=]|'[^'\s]*'|‘[^‘‘]*‘|\b\d+\b|\b[a-zA-Z#][a-zA-Z0-9#]*|\b[a-zA-Z#][a-zA-Z0-9#]*#|[^a-zA-Z0-9\s]", linea)
        print("tokens encontrados:",tokens)
        for token in tokens:
            print("token:",token)
            if token in palabras_reservadas:  # Identificar palabras reservadas
                lexema, valor = palabras_reservadas[token]
                tabla_lexica.append((num_linea, token, lexema, 1, valor, None))
                codigos_tokens.append(valor)
            elif token in delimitadores:  # Identificar delimitadores
                tipo, valor = delimitadores[token]
                tabla_lexica.append((num_linea, token, tipo, 5, valor, None))
                codigos_tokens.append(valor)
            elif token in operadores:  # Identificar operadores
                tipo, valor = operadores[token]
                tabla_lexica.append((num_linea, token, tipo, 7, valor, None))
                codigos_tokens.append(valor)
            elif re.match(r'^[0-9]+$', token): # Identificar constante numerica
                lexema = token
                tipo = 6
                tabla_constantes[lexema] = num_constante, 61
                tabla_lexica.append((num_linea, 'CONSTANTE', lexema, tipo, num_constante, None))
                num_constante += 1
            elif re.match(r"[‘']([a-zA-Z0-9\s]+)[‘']", token):  # Identificar constante 
                subtokens = re.findall(r"[‘']|[a-zA-Z0-9]+", token)  # Separar la constante en subtokens (comillas y constantes)
                print("subtoken:", subtokens)
                for subtoken in subtokens:
                    if subtoken in delimitadores:  # Si es una comilla
                        tipo,codigo = delimitadores[subtoken]
                        tabla_lexica.append((num_linea, subtoken, tipo, 5, codigo, None))  # Agregar a la tabla léxica
                        codigos_tokens.append(54)
                    else:  # Si es una constante
                        tipo = 6
                        lexema = subtoken[1:-1] if subtoken[0] in ["‘", "'"] else subtoken  # Extraer el lexema de la constante
                        codigo = num_constante
                        tabla_constantes[lexema] = num_constante,62
                        tabla_lexica.append((num_linea, 'CONSTANTE', lexema, tipo, num_constante, None))
                        codigos_tokens.append(62)
                        num_constante += 1
            # elif re.match(r"[‘']([a-zA-Z0-9]+)[‘']", token): # Identificar constante alfanumérica
            #     lexema = token[1:-1]
            #     tipo = 6
            #     tabla_constantes[lexema] = num_constante, 62
            #     tabla_lexica.append((num_linea, 'CONSTANTE', lexema, tipo, num_constante, None))
            #     codigos_tokens.append(62)
            #     num_constante += 1
            elif re.match(r'[a-zA-Z#][a-zA-Z0-9]*|[a-zA-Z#][a-zA-Z0-9#]*#', token) : # Identificar los identificadores
                if token not in tabla_identificadores:
                    tabla_identificadores[token] = num_identificador
                    num_identificador += 1
                lexema = f'ID_{tabla_identificadores[token]}'
                tabla_lexica.append((num_linea, token, lexema, 4, tabla_identificadores[token], None))
                codigos_tokens.append(4)
            elif re.match(r'[><=]', token):  # Identificar relacionales
                tipo, valor = relacionales[token]
                tabla_lexica.append((num_linea, token, tipo, 8, valor, None))
                codigos_tokens.append(8)
            else: #Atrapa los Errores
                errores.append((num_linea, f"Simbolo desconocido: {token}"))
                # Agregar el código de error a codigos_tokens
                codigos_tokens.append(token)
    
        num_linea += 1
    
    return tabla_lexica, tabla_identificadores, tabla_constantes, errores, codigos_tokens

def mostrar_errores(errores):
    if not errores:
        print("No se encontraron errores.")
    else:
        print("Se encontraron los siguientes errores:")
        for error in errores:
            num_linea, tipo_error = error
            print(f"Error en la línea {num_linea}: {tipo_error}")

def imprimir_tablas(tabla_lexica, tabla_identificadores, tabla_constantes):
    print("Tabla léxica:")
    print("| No. | Línea | TOKEN      | Tipo    | Código |")
    for idx, token in enumerate(tabla_lexica):
        if isinstance(token, tuple) and len(token) >= 5:
            num_linea, token_str, lexema, tipo, codigo = token[:5]
            codigo_str = codigo if codigo is not None else ''  
            print(f"| {idx+1:<4} | {num_linea:<5} | {token_str:<10} | {tipo:<7} | {codigo_str:<6} |")
        else:
            print(f"| {idx+1:<4} | {'':<5} | {token:<10} | {'':<7} | {'':<6} |")
    
    print("\nTabla de identificadores:")
    print("| Identificador | Valor | Línea |")
    for identificador, valor in tabla_identificadores.items():
        lineas = ', '.join(str(t[0]) for t in tabla_lexica if t[1] == identificador)
        print(f"| {identificador:<14} | {valor:<5} | {lineas} |")
    
    print("\nTabla de constantes:")
    print("| No. | Constante        | Tipo          | Valor |")
    constantes_indices = {}  
    for idx, (_, token, lexema, tipo, valor, _) in enumerate(tabla_lexica):
        if token == 'CONSTANTE':
            constantes_indices[lexema] = idx + 1  

    for lexema, (valor, tipo) in sorted(tabla_constantes.items(), key=lambda x: constantes_indices[x[0]]):
        tipo_nombre = 'ALFANUMERICO' if tipo == 62 else 'NUMERICO'
        print(f"| {constantes_indices[lexema]:<4} | {lexema:<16} | {tipo:<13} | {valor:<5} |")
def traducir(valorX):
    tipo=2
    descripcionError=""
    codigoError=-1;
    if 9<valorX<30 :
        descripcionError = "Se esperaba Palabra Reservada.";
        codigoError = 201;
        
    elif valorX== 4: # Identificador
        descripcionError = "Se esperaba Identificador.";
        codigoError = 204;
        
    elif 51<valorX<55:
        descripcionError = "Se esperaba Delimitador.";
        codigoError = 205;
       
    elif 60<valorX<63:
        descripcionError = "Se esperaba Constante.";
        codigoError = 206;
        
    elif 69<valorX<74: 
        descripcionError = "Se esperaba Operador.";
        codigoError = 207;
    elif valorX== 8:
        descripcionError = "Se esperaba Operador Relacional.";
        codigoError = 208;
        
    else:
        descripcionError = "Simbolo desconocido";
        codigoError = 101;
        tipo = 1;
        
    return tipo,codigoError,descripcionError

def algoritmo_ll(tabla_lexica):
    # Inicialización de la pila local
    pila = [199]
    # Insertar 300 en la pila
    pila.append(300)
    # Agregar '$' al final de codigos_tokens
    tabla_lexica.append(199)
    
    # Apuntador al primer TOKEN de Tabla Léxica
    apun = 0
    
    # Definición de X antes del bucle
    X = None
    print("pila INICIO:",pila)
    # Simulando un do-while con un bucle while
    while True:
        # Extraer elemento de la pila
        print("inicio ciclo pila antes POP:",pila)
        X = pila.pop()
        print("pila despues POP:",pila)
        K = tabla_lexica[apun]  # Obtener el TOKEN actual
        print("VALOR APUN:",apun)
        print("k= CODIGO TOKEN: ", K)
        print("x: ",X)
        # Condición de salida si X es '$'
        if X == 199:
            print("x=$: ", X)
            # Obtener el mensaje de error para el código 200
            return("todo bien")
            
        
      # Manejo de terminales y no terminales
        # if ((X > 9 and X < 30) or (X > 49 and X < 55) or (X>69 and X<74) or (X>60 and X<63)or X == 8 or X == 4) or X == 199:
        if (X<300) or X == 199:    
            print("x es terminal o $: ", X)
            print("valory:", K)

            if X == K:
                apun += 1  # Avanzar APUN
                K = tabla_lexica[apun]
                print("x = k, avanza apuntador:",apun )
            elif X != K:
                print("error X no es igual a K: valor esperado ", X)
                tipo, codigoError, descripcionError = traducir(x_valor)
                return "{} : {} {} Línea {}".format(tipo, codigoError, descripcionError, '')  # sin paréntesis ni comillas

        else:  # No es terminal
            print("X no es terminal o $:")
            print("valorx else:", X)
            print("valory else:", K)
            if tabla_sintactica[indices_estados[X]][indices_tokens[K]] != None:
                produccion = tabla_sintactica[indices_estados[X]][indices_tokens[K]]
                print("HAY PRODUCCION A ANADIR A LA PILA:", produccion)

                if produccion[0] != 99:  # Verificar si la producción no es 99
                    for elemento in reversed(produccion):
                        pila.append(elemento)
                        print("pila ACTUALIZADA:",pila)


                
            else:
            # Buscar el primer valor no nulo en la fila correspondiente a X en la tabla sintáctica
                seguir = True
                x_valor = None
                
                # for valor in tabla_sintactica[indices_estados[X]]: # no puede ser regla ni 99
                #     if valor is not None:
                #         x_valor = valor[0]
                #         break
                
                # X = x_valor
                # print("x_valor después del for:", x_valor)

                # while 300 <= x_valor <= 319 or x_valor==99:  # Si el resultado está entre 300 y 319, repetir el proceso
                #     for valor in tabla_sintactica[indices_estados[X]]:
                #         if valor is not None and valor[0] != 99 :
                #             x_valor = valor[0]
                #             break
                #     X = x_valor
                x_valor= primeros_ts[X]
                print("xvalor", x_valor)
                X = x_valor

                while 300 <= x_valor <= 319:  # Si el resultado está entre 300 y 319, repetir el proceso
                    x_valor= primeros_ts[X]
                    X = x_valor
                print("error2 valor x:", x_valor)

                tipo, codigoError, descripcionError = traducir(x_valor)
                return "{} : {} {} Línea {}".format(tipo, codigoError, descripcionError, '')  # sin paréntesis ni comillas


    
def main():
    while True:
        codigos_tokens = []
        print("\nIngrese la consulta SQL (o 'exit' para salir):")
        consulta = ""
        while True:
            linea = input()
            if linea.lower() == 'exit':
                return
            if not linea.strip():  
                break
            consulta += linea + "\n" 
        
        # Escaneo de entrada
        tabla_lexica, tabla_identificadores, tabla_constantes, errores, codigos_tokens = escanear_entrada(consulta.strip())

        # Si se encontraron errores, mostrarlos
        if errores:
            mostrar_errores(errores)
            
        else:
            # Impresión de las tablas de símbolos si no hay errores
            imprimir_tablas(tabla_lexica,tabla_identificadores,tabla_constantes)
            # Imprimir todos los códigos, incluyendo los errores
            print("\nArray de códigos de tokens:")
            print(codigos_tokens)

            # Ejecutar el algoritmo LL

            print(algoritmo_ll(codigos_tokens))

        

if __name__ == "__main__":
    main()
