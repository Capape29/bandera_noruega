from tkinter import *

bandera_noruega = Tk()

# Titulo de la ventana
bandera_noruega.title(" Bandera Noruega ")

# Dimensiones o tamaño de la ventana
bandera_noruega.geometry("800x500")

# Desabilitar boton de maximizar
bandera_noruega.resizable(0,0)

# Color de fondo de la ventana
bandera_noruega.config(bg = "red")
frame_blanco_vertical = Frame(bandera_noruega)
frame_blanco_vertical.config(bg = "snow", width = 110, height = 500)
frame_blanco_vertical.place(x = 190, y = 0)

frame_blanco_horizontal = Frame(bandera_noruega)
frame_blanco_horizontal.config(bg = "snow", width = 800, height = 110)
frame_blanco_horizontal.place(x = 0, y = 190)

frame_azul_vertical = Frame(bandera_noruega)
frame_azul_vertical.config(bg = "navy", width = 54, height = 500)
frame_azul_vertical.place(x = 220, y = 0)

frame_azul_horizontal = Frame(bandera_noruega)
frame_azul_horizontal.config(bg = "navy", width = 800, height = 54)
frame_azul_horizontal.place(x = 0, y = 220)


# Se ejeccuta el metodo mainloop() de la clase Tk a través de la instancia ventana_principal. Esta metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (clic en un boton, escribir, etc) Cada acción del usuario se conoce como un evento. El método mainloop()es un bucle infinito.
bandera_noruega.mainloop()