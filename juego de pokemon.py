import random

Ps_jugador= 100
Ps_oponente= 100
defensa_oponente=100
defensa_jugador=100
ataques_usados=[] #lista de los ataques usados

#ataqques = [aascua, sjsj, asas]
while Ps_jugador >0 and Ps_oponente >0:
    ataque_jugador= input("ataque: ")
    ataque_jugador = ataque_jugador.lower()
    ataques_usados.append(ataque_jugador) #agrega a la lista los ataques que se usaron en la batalla
    if ataque_jugador== "malicioso":
        defensa_oponente -= 10 #=defensa_oponente-10
        if defensa_oponente<=0:
            defensa_oponente=1
    elif ataque_jugador == "placaje":
        Ps_oponente -= 35 / (defensa_oponente/100)
    elif ataque_jugador == "ascuas":
        Ps_oponente-=20
    else:
        print("Que estas haciendo? ! Tus ataques son malicioso, placaje y ascuas")
        continue

    #turno del oponente
    ataque_oponente = random.randrange(1,3+1)
    if ataque_oponente ==1: #latigo
        defensa_jugador -= 10
        if defensa_oponente <= 0:
            defensa_oponente= 1
    elif ataque_oponente== 2: #place
        Ps_jugador-=35 * (100/defensa_jugador)
    elif ataque_oponente== 3: #pistola de agua
        Ps_jugador -=40
#randrage esta garantizado a ser 1, 2 o 3
if Ps_oponente <=0:
    print("Felicidades, has ganado")
else: #ya sabemos que el oponente es > 0
    print ("Lo siento, has perdido")
print("Usaste los ataques", ataques_usados)