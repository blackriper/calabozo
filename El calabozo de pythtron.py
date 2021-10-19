import random


#Variables del juego
tiro_dado=0
hizo_desafio_1=False
hizo_desafio_2=False
hizo_desafio_3=False
hizo_desafio_4=False
escogio_espada_cuantica=False
escogio_libro_pylion=False
obtuviste_llave_izquierda=False
obtuviste_llave_derecha=False
escogio_elemento_ec2=False
escogio_caja_cuantix=False


print("El calabozo de pythtron\n")

print(" pythtron era un ser cuantico el cual disfrutaba de crear cosas pero con el paso de los siglos se aburrio,\n"
      " penso que para matar el tiempo  seria divertido conquistar otros mundos fuera de su plano cuantico.\n"
      " pythtron logro acumular grandes tesoros a lo largo  de sus conquistas,un dia se aburrio de ello.\n"
      " creo un calabozo donde guardo su gran tesoro y quien quisiera podria tomarlo pero sopresa!\n"
      " pythtron es un loquillo el cual ademas de crear cosas se hizo aficionado alos combates y a los problemas matematicos\n")

print("Bienvenido al calabazo de pythtron un lugar que puede darte gloria o una muerte inminente\n ")

print("has entrado al calabozo hay una especie de recepcion solo hay alguien parado")

print("saludos desafiante  soy nodetrix uno de los guardianes del calabazo\n"
      "el calabozo se compone de 4 pisos, el piso cuatro se desbloqueara\n "
      "cuando tengas los elementos necesarios.\n")

opcion1=input("\nHay dos formas de decender del calabozo una forma es usando el dado random el cual te lleva a un piso al azar\n"
      " pero te he de avisar que si caes en el piso cero que es la recepcion todo se acabo. la otra forma de avanzar\n"
      " es contestando un problema y avanzaras al piso 1.\n"
      "  A- Dado random\n"
      "  B- Contestar problema\n ")

if opcion1=="A":
    tiro_dado= random.randint(0,3)
    if tiro_dado==0:
          print("Has muerto tu travesia termina antes de empezar\n")
          exit()
    else:
      print( "\nHas caido al piso"+str(tiro_dado))

elif opcion1=="B":
      # varible que determinal el numero a multiplicar
      multiplicador=random.randint(1,10)
      res_py=12*multiplicador;
      res_us= float(input("¿Cuanto es 12*{} ?".format(multiplicador)))
      if res_us==res_py:
            print("\nFelicidades has  desendido al piso 1\n")
            hizo_desafio_1=True
      else:
            print("Has muerto tu travesia termina antes de empezar\n")
            exit()


if  tiro_dado==1 or hizo_desafio_1:
     print("Has asendio al piso 1 es una especie de bosque oscuro \n"
           "donde aquellos que no lograron pasar de piso sus almas son atrapadas aqui"
           "a lo lejos se aproxima alguien montado en un caballo\n")

     print("\nUn caballero sosteniendo se cabeza se acerca  saludos desfiante\n"
           "soy el guardian de este piso dullahan y para pasar al siguiente\n"
           " piso debes decir si el numero que aparece es par o inpar\n")
     #numero aleatorio del 1 al 100
     numero=random.randint(1,100)
     if numero % 2 == 0:
         que_es="P"
     else:
         que_es="IM"

     answer= input("\nEl numero {} es par[P] o impar[IM]\n ".format(numero))
     if answer== que_es:
         #la variable pasa a true despues de la decision del usuario
         arma= int(input("\nHaz contestado correctamente  como recompensa puedes escoger alguno\n"
                     "de  alguno de los siguientes reliquias ¡Escogeos bien desafiente!\n"
                     "\n1-La espada cuantica una espada que en las manos correctas podria derrotar a pythtron\n"
                     "2-El pylion libro de tips escrito por pyhtron  para facilitar tu travesia en el calabozo\n "))
         if arma==1:
             escogio_espada_cuantica=True
             texto="La espada cuantica"
         else:
             escogio_libro_pylion=True
             texto="El pylion"

         hizo_desafio_2=True
         print("\nHas escogido "+texto+" puedes pasar al piso 2\n")

     else:
         print("El juego a termindo para ti pero no te preocupes\n"
               " tandras todo el tiempo del mundo en este bosque para pensar lo que hiciste mal ")
         exit()


if tiro_dado==2 or hizo_desafio_2:
    print("\nHaz bajado al piso 2 a comparacion del primer piso este piso es\n"
          " un gran campo vacio sonde solo se escucha el sonido del viento\n"
          " solo hay una pequeña mesa donde hay alguien esperedando\n"
          " al acercate mas a la mesa te das cuenta que es nodetrix\n"
          " quien te dio la bienvenida en el piso 0.\n")

    if escogio_libro_pylion:
        leer=input("¿puedes leer el pylion para saber mas de nodetrix?  s/n\n")
        if leer=="s":
            print("nodetrix es un ser que le gusta jugar ajedrez si hablas sobre el tema puede que te deje pasar al piso tres\n ")
            res=input("¿Hablar sobre ajedrez con nodedrix s/n?")
            if res=="s":
                print("no pareces del tipo que juegue ajedrez, te pondre a prueba si contestas correctamente a mi pregunta\n"
                      " te dejare pasar al piso 3 y te dare una recompensa\n")
                quiz=input("¿ El afil Se mueve en diagonal, no puede saltar piezas intervinientes,\n"
                           " y captura tomando el lugar ocupado por la pieza adversaria [C] cierto [F] falso?\n")

                if quiz=="C":
                   prize= int(input(" oh has contestado bien puedo darte las sigientes recompensas\n"
                          "1- La llave de la puerta izquierda del piso 4\n"
                          "2- Elemento Ec2 los seres cuanticos lo usan como alimento\n"))

                   if prize == 1:
                       obtuviste_llave_izquierda = True
                       texto = " La llave izquierda"
                   else:
                       escogio_elemento_ec2 = True
                       texto = "El Elemento ec2"

                   hizo_desafio_3 = True
                   print("\nHas escogido " + texto + " puedes pasar al piso 3\n")
                else:
                    print("\nlastima pero aqui termina el juego sientete afortunado te convertiras en una\n"
                          " de las piezas de mi tablero para la eternidad\n")
                    exit()
            else:
                quiz = input("¿ El caballo en ajedrez Tiene un movimiento semejante a una 'L' y, a diferencia de otras piezas\n"
                             " y captura tomando el lugar ocupado por la pieza adversaria [C] cierto [F] falso?\n")
                if quiz == "C":
                    prize = int(input("\n oh! has contestado bien puedo darte las sigientes recompensas\n"
                                      "\n1- La llave de la puerta izquierda del piso 4\n"
                                      "\n2- Elemento Ec2 los seres cuanticos lo usan como alimento\n"))

                    if prize == 1:
                        obtuviste_llave_izquierda = True
                        texto = " La llave izquierda"
                    else:
                        escogio_elemento_ec2 = True
                        texto = " El Elemento ec2"

                    hizo_desafio_3 = True
                    print("\nHas escogido  " + texto + " puedes pasar al piso 3\n")
                else:
                    print("\nlastima pero aqui termina el juego sientete afortunado te convertiras en una\n"
                          " de las piezas de mi tablero para la eternidad\n")
                    exit()

    elif escogio_espada_cuantica:
        res=int(input("nos vemos de nuevo si quieres llegar al piso 3 primero tienes que solucionar  este problema\n" 
              "adivina un numero del 1 al 10\n"))

        adivinar_numero=random.randint(1,10)

        if res==adivinar_numero:
            prize = int(input(" \n oh! has contestado bien puedo darte las sigientes recompensas\n"
                              "\n1- La llave de la puerta derecha  del piso 4\n"
                              "\n2- Caja cuantix puede encerrar a seres cuanticos menos a su creador pythtron\n"))

            if prize == 1:
                obtuviste_llave_derecha = True
                texto = " La llave derecha"
            else:
                escogio_caja_cuantix = True
                texto = "Caja Cuantix"

            hizo_desafio_3 = True
            print("Has escogido " + texto + " puedes pasar al piso 3\n")
        else:
            print("\nlastima pero aqui termina el juego \n")
            exit()

    else:
        print("\nHas llegaado hasta aqui usando el dado Random lastima pero a los que toman atajos \n"
              "solo pueden terminar en la prision cuantica\n")
        exit()



if tiro_dado==3 or hizo_desafio_3:
    print("\nEl tercer piso es el alamcen donde pythron guarda sus inventos\n"
          " con algo de suerte y puedes llevarte algun artefacto de utilidad\n"
          "pero este piso es custidiado por el dragon cuantico un gran dragon\n"
          " creado por pythron para cuidar sus cosas\n")

    if escogio_elemento_ec2:
        print(" \nComo elegiste el elemento Ec2 alimentaste al dragon cuantico\n"
              " este te entrega el teletrasportador pip como agradecimiento.\n"
              " en hora buena haz podido salir del calabozo\n")

        print("\npero te preguntaras porque no  llegaste al ultimo piso es sencillo\n"
              " el piso cuatro solo tiene dos puertas y necesitas la llave para poder entrar\n")
        exit()
    elif escogio_libro_pylion:
       con=input("puedes leer el pylion para saber mas del dragon cuantico s/n\n")
       if con=="s":
           res=input("El dragon cuantico es muy sabio y disfruta de los quiz de preguntas\n"
                 " si juegas con el podrias pasar al otro piso,\n"
                 "¿Quieres jugar con el dragon cuantico s/n\n")
           if res=="s" and obtuviste_llave_izquierda:
               af=input("¿ Guglielmo Marconi invento la radio s/n?")
               if af=="s":
                   print("\nFelicidades haz pasado al ultimo piso y llevas contigo la llave para la puerta izquierda\n")
                   hizo_desafio_4=True
               else:
                   print("\nllevas una herramienta que no usas !que sentido tiene! muere por tu arrogancia por no querer recibir ayuda\n")
                   exit()


    elif escogio_espada_cuantica:
        if escogio_caja_cuantix:
            print("\nHaz logrado usar la Caja cuantix  haz encerrado al dragon cuantico."
                  " increible pythron ha aparecido en persona y te felicita por haber vencido\n"
                  "al dragon pero aun asi no eres digno de pisar el cuarto piso toma el teletrasportador pip\n"
                   "en hora buena haz podido salir del calabozo\n")

            print("\npero te preguntaras porque no  llegaste al ultimo piso es sencillo\n"
                  " el piso cuatro solo tiene dos puertas y necesitas la llave para poder entrar\n")
        else:
            opcion=input("Para poder pasar necesitas responder mi pregunta\n"
                         "\n ¿En que año acabo la segunda guerra mundial?\n"
                         "a-1939"
                         "b-1930"
                         "c-1945")
            if opcion=='c' and obtuviste_llave_derecha:
                print("Eres digno de pasar al cuarto piso y veo que tambien tienes la llave de la puerta derecha")
                hizo_desafio_4 = True
            else:
               print("\nEl peor esenario posible pythron la aparecido y como tienes la espada cuantica\n"
                     " ha decido retarte a una gran batalla peleaste con todo,\n"
                     "pero al final haz muerto seras recordado como un gran guerrero.\n")
               exit()
    else:
        print("\nHas llegaado hasta aqui usando el dado Random lastima pero a los que toman atajos \n"
              "solo pueden terminar en la prision cuantica\n")
        exit()

if hizo_desafio_4:
    print("\nDespues de mucho haz superado las pruebas y llegado al ultimo piso\n "
          "El ultimo piso solo tiene dos puertas")

    if obtuviste_llave_derecha:
        print("\nComo tienes la llave derecha haz llegado al enemigo final\n"
              " pyhtron la batalla ha comenzado la espada cuantica daña\n"
              " a pyhtron pero para derrotarlo necesitas\n")
        ultima=input("\nAcompletar la siguiente serie de fibonacci 1, 2, 3, 5, 8, 13, 21, 34 ¿cual es el numero que sigue?\n"
                     "a-23\n"
                     "b-55\n"
                     "c-90\n")
        if ultima=="b":
            print("Lo has logrado pythron no puede morir pero al menos las heridas que le has causado\n"
                  " lo dejaran quieto un par de años en hora buena el tesoro es tuyo ha salido con vida y con un gran tesoro.\n")
            exit()
        else:
            print("Seras recordado como el heroe que casi derroto a pythron tu nombre no sera olvidado\n")
            exit()

    elif obtuviste_llave_izquierda:
        print(" como tienes la llave de la puerta izquierda oh haz caido en  la prision cuantica donde pythtron\n"
              " encierra a sus enemigos que derrota ,algunas veces obtener respuestas a los problemas no es lo mejor\n"
              "pythron es un loquillo por naturaleza porque ayudararia a alguien en primer lugar, simple es divertido para el\n "
              " ¡Señor pythtron usted es diabolico!\n")
        exit()





