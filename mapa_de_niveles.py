
def convierte_en_nivel(operaciones: str = ""):

    operaciones = operaciones.replace(" ", "")
    operaciones = operaciones.replace("x", "*")
    mapa_de_niveles = []

    for i in operaciones:  # creamos el mapa de niveles
        if not i in "()":
            if i.isnumeric():
                mapa_de_niveles.append(int(i))
            else:
                mapa_de_niveles.append(i)
        else:
            mapa_de_niveles.append(i)
    niveles = mapa_de_niveles.count("(")
    operaciones_ordenadas = []
    for i in range(niveles+1):
        operaciones_ordenadas.append([])

    nivel = 0
    for i in mapa_de_niveles:

        if i != "(" and i != ")":
            operaciones_ordenadas[nivel].append(i)
        elif i == "(":
            nivel += 1
        elif i == ")":
            nivel -= 1

    return operaciones_ordenadas


if __name__ == "__main__":
    print(convierte_en_nivel("Hola(esto(es(un(mapa(de(niveles))))))")) 
