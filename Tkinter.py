import tkinter as tk
import Funciones_crud

ventana = tk.Tk()
ventana.title("Fauna y Flora - Software")
ventana.attributes("-alpha", 0.9)
ventana.configure(bg="gray91")

#Frames

frame_nombre_habitat = tk.Frame(ventana)
frame_nombre_habitat.pack(pady=10)

frame_informacion_especie = tk.Frame(ventana)
frame_informacion_especie.pack(pady=10)

frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

#Label, entry y menu

    #frame_nombre
label_nombre = tk.Label(frame_nombre_habitat, text="Nombre de la especie: ")
label_nombre.grid(row=0, column=0, padx=5, pady=5)
label_habitat = tk.Label(frame_nombre_habitat, text="Habitat: ")
label_habitat.grid(row=1, column=0, padx=5, pady=5)

Funciones_crud.entry_nombre = tk.Entry(frame_nombre_habitat)
Funciones_crud.entry_nombre.grid(row=0, column=1, padx=5, pady=5)
Funciones_crud.entry_habitat = tk.Entry(frame_nombre_habitat)
Funciones_crud.entry_habitat.grid(row=1, column=1, padx=5, pady=5)

    #frame_informacion_especie
estado_especie = ["Vulnerable","Preocupación menor", "En peligro", "Conservado"]
region_especie = ["Africa", "Europa", "Sudeste Asiático", "América del sur", "América del norte", "Centroamérica", "Oceanía", "Asia"]
Funciones_crud.var_estado_especie = tk.StringVar()
Funciones_crud.var_region_especie = tk.StringVar()


label_estado_especie = tk.Label(frame_informacion_especie, text="Información de la especie:")
label_estado_especie.grid(row=0, column=0, padx=5, pady=5)
label_region_especie = tk.Label(frame_informacion_especie, text="Región donde habita:")
label_region_especie.grid(row=1, column=0, padx=5, pady=5)

menu_estado_especie = tk.OptionMenu(frame_informacion_especie, Funciones_crud.var_estado_especie, *estado_especie)
menu_estado_especie.grid(row=0, column=1, padx=5, pady=5)
menu_region_especie = tk.OptionMenu(frame_informacion_especie, Funciones_crud.var_region_especie, *region_especie)
menu_region_especie.grid(row=1, column=1, padx=5, pady=5)

    #Frame botones

label_id_especie = tk.Label(frame_botones, text="ID a eliminar: ")
label_id_especie.grid(row=1, column=0, padx=5, pady=5)

Funciones_crud.entry_id_especie = tk.Entry(frame_botones)
Funciones_crud.entry_id_especie.grid(row=1, column=1, padx=5, pady=5)

btn_agregar_especie = tk.Button(frame_botones, text="Agregar especie", command=Funciones_crud.agregar_especie)
btn_agregar_especie.grid(row=0, column=0, padx=5, pady=5)

btn_mostrar_especie = tk.Button(frame_botones, text="Mostrar datos", command=Funciones_crud.mostrar_especie)
btn_mostrar_especie.grid(row=0, column=1, padx=5, pady=5)

btn_eliminar_especie = tk.Button(frame_botones, text="Eliminar registro", command=Funciones_crud.eliminar_especie)
btn_eliminar_especie.grid(row=2, column=1, padx=5, pady=5)

ventana.mainloop()