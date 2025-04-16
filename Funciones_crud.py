import tkinter as tk
from tkinter import messagebox
import conexion_db

tabla = "faunaflora"

def agregar_especie():
    nombre_especie = entry_nombre.get()
    habitat_especie = entry_habitat.get()
    estado_especie = var_estado_especie.get()
    region_especie = var_region_especie.get()
    try:
        conexion = conexion_db.conectar_db()
        cursor = conexion.cursor()

        cursor.execute(f"INSERT INTO {tabla} (nombre_cientifico, habitat, estado_conservacion, region_geografica) values (%s, %s, %s, %s)", (nombre_especie, habitat_especie, estado_especie, region_especie))

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Registro completado", "Especie registrada con éxito")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurriò un problema con el llenado:\n{e}")

def mostrar_especie():
    try:
        conexion = conexion_db.conectar_db()
        cursor = conexion.cursor()

        consulta_select = f"select * from {tabla}"

        cursor.execute(consulta_select)

        resultados = cursor.fetchall()

        mensaje = ""
        for resultado in resultados:
            mensaje += f"ID: {resultado[0]} | Nombre: {resultado[1]} | Habitat: {resultado[2]} | Estado: {resultado[3]} | Región: {resultado[4]}\n\n"

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Información de la base de datos", mensaje)

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un problena con la visualización:\n{e}")

def eliminar_especie():
    try:
        id_especie = entry_id_especie.get()

        conexion = conexion_db.conectar_db()
        cursor = conexion.cursor()

        borrar_registro = f"delete from {tabla} where id = %s"

        cursor.execute(borrar_registro, (id_especie,))

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Registro eliminado", "Especie eliminada de la base de datos.")

    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar el registro")

def actualizar_informacion():
    try:
        id_especie = entry_id_especie.get()
        nombre_especie = entry_nombre.get()
        habitat_especie = entry_habitat.get()
        estado_especie = var_estado_especie.get()
        region_especie = var_region_especie.get()

        if not id_especie:
            messagebox.showerror("Sin ID", "Ingresa el ID a modificar")
            return

        conexion = conexion_db.conectar_db()
        cursor = conexion.cursor()

        actualizar = f"update {tabla} set nombre_cientifico = %s, habitat = %s, estado_conservacion = %s, region_geografica = %s where id = %s"

        cursor.execute(actualizar, (nombre_especie, habitat_especie, estado_especie, region_especie, id_especie))

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Información de la base de datos actualizada", "Se realizan cambios correspondientes")

    except Exception as e:
        messagebox.showerror("Error", "No se pudo actualizar la información")




