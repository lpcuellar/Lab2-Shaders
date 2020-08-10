##
##  UNIVERSIDAD DEL VALLE DE GUATEMALA
##  GRÁFICAS POR COMPUTADORA
##  SECCIÓN 20
##
##  LAB2: SHADERS
##  LUIS PEDRO CUÉLLAR - 18220
##

from gl import Render, color, norm
from object import Object, Texture
from shaders import gourad, toon

render = Render(1000, 1000)
title = "---    APLICAR SHADERS A MOBDELOS OBJ    ---\n"
main_menu = """Opciones:
        1. Cambiar color de fondo (default = negro)
        2. Aplicar toon shader a una cara
        3. Aplicar gourad shader a una cara
        4. Aplicar toon shader a la tierra
        5. Aplicar gourad shader a la tierra
        6. Salir
        """

wants_to_continue = True
option = 0
r = 0
g = 0
b = 0
are_values_ok = False

print(title)
while(wants_to_continue):
    print(main_menu)
    option = input("        Ingrese la opción que desea realizar: ")
    option = int(option)

    ##  changes the background color of the image
    if(option == 1):
        is_values_ok = False

        ## ask the values for the rgb and check that they are valid
        while(is_values_ok == False):
            r = input("Ingrese el valor r del color deseado (de 0 a 1): ")
            r = float(r)
            g = input("Ingrese el valor g del color deseado (de 0 a 1): ")
            g = float(g)
            b = input("Ingrese el valor b del color deseado (de 0 a 1): ")
            b = float(b)

            if((r < 0 or r > 1) or (g < 0 or g > 1) or (b < 0 or b > 1)):
                print("\nPor favor escoger valores entre 0 y 1\n")
            else:
                is_values_ok = True

                ##  changes the background color of the image
                render.glClearColor(r, g, b)

    ##  apply toon shader to a face
    elif(option == 2):
        render.current_texture = Texture('./textures/model.bmp')
        render.current_shader = toon
        render.loadModel('./models/model.obj', (500, 500, 0), (1, 1, 1), False)
        render.glFinish("toonFace.bmp")
        print("Termiado!")
        wants_to_continue = False

    ##  apply gourad shader to a face
    elif(option == 3):
        render.current_texture = Texture('./textures/model.bmp')
        render.current_shader = gourad
        render.loadModel('./models/model.obj', (500, 500, 0), (1, 1, 1), False)
        render.glFinish("gouradFace.bmp")
        print("Termiado!")
        wants_to_continue = False

    ##  apply toon shader to a face
    elif(option == 4):
        render.current_texture = Texture('./textures/earthDay.bmp')
        render.current_shader = toon
        render.loadModel('./models/earth.obj', (500, 500, 0), (1, 1, 1), False)
        render.glFinish("toonEarth.bmp")
        print("Termiado!")
        wants_to_continue = False

    ##  apply gourad shader to a face
    elif(option == 5):
        render.current_texture = Texture('./textures/earthDay.bmp')
        render.current_shader = gourad
        render.loadModel('./models/earth.obj', (500, 500, 0), (1, 1, 1), False)
        render.glFinish("gouradEarth.bmp")
        print("Termiado!")
        wants_to_continue = False

    ##  exits the program
    elif(option == 6):
        wants_to_continue = False
        print("BYEEE")

    else:
        print("Por favor escoja una opción válida!")
