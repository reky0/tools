import time
import os
import getpass
from csv import writer
import webbrowser

#para cada vez que se abre la ubicacion del archivo
usuario_actual = getpass.getuser()

#imprime un menú y da a elegir tres opciones posibles, si no se introduce ninguna de ellas se reconoce y se avisa como errónea
def menú_de_inicio():
    os.system('cls')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('                                                        EUTERKYO                                                       ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    print('1 - Elegir canción')
    print('2 - Ampliar registros')
    print('3 - Playlists')
    print('4 - Salir')
    while True:
        opcion_menu = input('\n')
        if opcion_menu == '1':
            elegir_cancion()
        elif opcion_menu == '2':
            ampliar_registros()
        elif opcion_menu == '3':
            menu_playlist()
        elif opcion_menu == '4':
            os.system('cls')
            exit()
        else:
            #por si lo introducido no está registrado como una opción
            print('La opción introducida no es válida, introduce una de nuevo')
            time.sleep(3)
            menú_de_inicio()

#como dice el nombre del módulo, es el encargado de la elección y reproducción de la canción elegida
def elegir_cancion():
    while True:
        os.system('cls')
        #intrucciones de elección
        print('Elige una canción introduciendo su número identificador. Introduce \'*\' para volver al menú.\n\n')
        #variable con todas las líneas del documento
        with open('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO/lista de canciones.csv', 'r') as f:
            lines = f.read().split('\n')

        #impresión del archivo sustituyendo ; por | para una mejor y más fácil lectura de la lista
        with open('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO/lista de canciones.csv', 'r') as lista:
            print(lista.read().replace(';', ' | '))
            
        #introduccion de la opción deseada por parte del usuario
        cancion = input()

        #condicionales que valoran la posibilidad de que el usuario quiera salir de este modo, espacios en la entrada de datos, ausencia de datos o caracteres alfabéticos en la cadena introducida, lo cual es incorrecto puesto que los identificadores son únicamente números
        if cancion == '*':
            menú_de_inicio()
        elif cancion == '':
            print('No has introducido ninguna opción.')
        elif ' ' in cancion:
            print('No se admiten espacios en blanco')
        elif cancion.isdigit() == True:
            #crea una variable que sea la línea entera de la canción elegida
            for line in lines:
                if line.startswith(cancion + ';'):
                    linea_elegida = line
                else:
                    pass
            
            #crea un array que contenga las posiciones de los ; de la línea elegida
            posiciones_puntos_y_coma = [idx for idx, x in enumerate(str(linea_elegida)) if x == ';']
            #le quitamos el ] final para ahorrarnos problemas a la hora de seleccionar el enlace
            posiciones_puntos_y_coma = str(posiciones_puntos_y_coma).replace(']','')
            #averiguamos las posiciones de las , del array creado anteriormente
            posiciones_coma = [idx for idx, x in enumerate(str(posiciones_puntos_y_coma)) if x == ',']
            #también le quitamos el ] final por el mismo motivo que antes
            posiciones_coma = str(posiciones_coma).replace(']', '')
            #el comienzo del enlace de la canción de la línea elegida comienza en la posición número 5 del array de las comas +2 posiciones más
            tercer_punto_y_coma = str(posiciones_coma)[4:]
            tercer_punto_y_coma = posiciones_puntos_y_coma[int(tercer_punto_y_coma)+2:]
            
            #el enlace de la canción va desde la posición del tercer ; +1 hasta el final de la cadena
            enlace_cancion = linea_elegida[int(tercer_punto_y_coma)+1:]

            #buscamos el enlace abriendo una conexión con el buscador en una pestaña nueva
            webbrowser.open(enlace_cancion, new=1, autoraise=True)
        elif cancion.isalpha() == True:
            print('Los identificadores no contienen caracteres alfabéticos. Introduce un número identificador de nuevo')


        time.sleep(3)

#comprueba que el archivo que usamos de lista de las canciones exista, en caso de que no, lo crea, igual que con la carpeta que lo contiene
def comprobar_archivo():
    #comprobamos si existe la carpeta, en caso contrario la crea
    if os.path.isdir('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO'):
        #comprobamos que existe el archivo, en caso contrario lo crea
        if os.path.isfile('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO/lista de canciones.csv'):
            pass
        else:
            file = open('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO/lista de canciones.csv', 'w')
            file.write('id;artista;canción;enlace\n')
            file.close()
    else:
        #creamos el directorio y realizamos el mismo proceso con el archivo que antes
        os.mkdir('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO')
        if os.path.isfile('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO/lista de canciones.csv'):
            pass
        else:
            file = open('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO/lista de canciones.csv', 'w')
            file.write('id;artista;canción;enlace\n')
            file.close()

def ampliar_registros():
    #abrimos un bucle para hacerlo más ágil en caso de realizar el proceso más veces
    while True:
        #pregunta por los datos requieridos
        enlace_cancion = input('\n¿Cuál es el enlace del vídeo?:  ')
        artista = input('¿Cómo se llama el artista o grupo?:  ')
        nombre_cancion = input('¿Cómo se llama la canción?:  ')

        #pide una confirmación al usuario de los datos previamente introducidos
        print('\nEl enlace introducido es: ' + enlace_cancion)
        print('El nombre del artista introducido es: ' + artista)
        print('El nombre de la canción es: ' + nombre_cancion)

        confirmar_datos = input('\n¿Es esta información correcta?[s/n]:  ')

        #si son correctos los datos, inicia el proceso de ampliación de los registros
        if confirmar_datos == 's':
            with open('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO/lista de canciones.csv') as f:
                #verifica que el enlace del nuevo registro no está registrado ya
                if enlace_cancion in f.read():
                    #le da la opción al usuario de añadir otro registro o volver al menú
                    print('En enlace de la canción ya está registrado. Pulse intro para volver a introducir otros datos o introduzca "*" para salir del modo de ampliación de registros.')
                    enlace_repetido = input()
                    if enlace_repetido == '*':
                        menú_de_inicio()
                    else:
                        pass
                else:
                    #empieza la actualización de los registros una vez sabe que es uno nuevo el que va a añadir
                    print('\nDe acuerdo, guardaré estos datos, espera un momento')

                    #obtiene la última línea del archivo
                    with open('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO/lista de canciones.csv', 'r') as f:
                        ultima_linea = f.readlines()[-1]
                    
                    #obtiene todas las líneas del archivo
                    with open('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO/lista de canciones.csv', 'r') as fi:
                        lineas = fi.read().split('\n')

                    #recorre todo el archivo buscando cuál es el máximo número de cifras que tiene el identificador más alto
                    modo = 0
                    for line in lineas:
                        if line.startswith('id;'):
                            modo = 1
                        elif line.startswith('1;'):
                            modo = 1
                        elif line.startswith('2;'):
                            modo = 1
                        elif line.startswith('3;'):
                            modo = 1
                        elif line.startswith('4;'):
                            modo = 1
                        elif line.startswith('5;'):
                            modo = 1
                        elif line.startswith('6;'):
                            modo = 1
                        elif line.startswith('7;'):
                            modo = 1
                        elif line.startswith('8;'):
                            modo = 1
                        elif line.startswith('9;'):
                            modo = 1
                        elif line.startswith('10;'):
                            modo = 2
                        elif line.startswith('100;'):
                            modo = 3
                        else:
                            pass

                    #dependiendo del número de cifras del identificador más grande tomará más o menos cifras como identificador
                    if modo == 1 or modo == 0:
                        identificador = ultima_linea[0]
                    elif modo == 2:
                        identificador = ultima_linea[0:2]
                    elif modo == 3:
                        identificador = ultima_linea[0:3]

                    #tras comprobar que el identificador es un número, se actualiza sumándole 1 porque el nuevo será el siguiente al último
                    if str(identificador).isdigit() == True:
                        identificador = int(identificador) + 1
                    else:
                        #si no es un número quiere decir que es el encabezado del documento, y por tanto lo establece como 1 al ser el primero
                        identificador= str(1)

                    #crea un array con todos los datos introducidos más el identificador
                    datos_a_introducir = [str(identificador) + ';' + artista + ';' + nombre_cancion + ';' + enlace_cancion]
                    
                    #añade el array anteriormente creado al archivo
                    with open('C:/Users/' + usuario_actual + '/Desktop/EUTERKYO/lista de canciones.csv', 'a', newline='') as f_object:  
                        # Pass the CSV  file object to the writer() function
                        writer_object = writer(f_object)
                        # Result - a writer object
                        # Pass the data in the list as an argument into the writerow() function
                        writer_object.writerow(datos_a_introducir)  
                        # Close the file object
                        f_object.close()

                    #le da la opción al usuario de añadir más registros
                    volver_a_ampliar = input('¿Quieres añadir más registros?[s/n]:  ')

                    #si elige añadir más, pasará y volverá a empezar el proceso puesto que estamos en un bucle. Si elige que no, volverá al menú principal
                    if volver_a_ampliar == 's':
                        pass
                    elif volver_a_ampliar == 'n':
                        menú_de_inicio()
        elif confirmar_datos == 'n':
            #si en la confirmación el usuario dice que no son correctos, el programa pedirá todos los datos de nuevo ya que está en un bucle
            print('\nIntroduce los datos de nuevo')

def menu_playlist():
    os.system('cls')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('                                                      PLAYLISTS')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n1 - Elegir canción')
    print('2 - Ampliar registros')
    print('3 - Playlists')
    print('4 - Salir')
    while True:
        opcion_menu = input('\n')
        if opcion_menu == '1':
            elegir_cancion()
        elif opcion_menu == '2':
            ampliar_registros()
        elif opcion_menu == '3':
            menu_playlist()
        elif opcion_menu == '4':
            os.system('cls')
            exit()
        else:
            #por si lo introducido no está registrado como una opción
            print('La opción introducida no es válida, introduce una de nuevo')
            time.sleep(3)
            menú_de_inicio()


#en primer lugar ejecuta el módulo de comprobación y seguido empieza el menú
comprobar_archivo()
menú_de_inicio()