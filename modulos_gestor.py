# 1. Añadir tarea
def añadir_tarea(tareas, nombre_tarea):
    # tarea: nombre de la tarea
    # completada: indicar si esta tarea ya ha sido completada o no.
    tarea = {'tarea': nombre_tarea, 'completada': False}
    tareas.append(tarea)
    print(f'\n> ¡La tarea {nombre_tarea} ha sido añadida con éxito!')
    return

# 2. Ver tareas
def ver_tareas(tareas):
    if tareas == []:
        print('\n> ¡No tienes tareas!\n¡Escribe [1] para añadir una nueva tarea!')
    else:
        print('\nLista de tareas:')
        for índice, tarea in enumerate(tareas, start=1):
            
            estado = '✓' if tarea['completada'] == True else ' '

            print(f'Tarea {índice}: [{estado}] {tarea['tarea']}')
    return

# 3. Actualizar tarea
def actualizar_nombre_tarea(tareas, indice_tarea, nuevo_nombre_tarea):
    indice_tarea_ajustado = int(indice_tarea) - 1
    if indice_tarea_ajustado >= 0 and indice_tarea_ajustado < len(tareas):
        tareas[indice_tarea_ajustado]['tarea'] = nuevo_nombre_tarea
        print(f'Tarea {indice_tarea} actualizada a: {nuevo_nombre_tarea}')
    else:
        print('\n¡¡¡ÍNDICE DE TAREA INVÁLIDO!!!')
    return

# 4. Marcar como completada
def marcar_como_completada(indice_tarea, tareas):
    indice_tarea_ajustado = int(indice_tarea) - 1
    if indice_tarea_ajustado >= 0 and indice_tarea_ajustado < len(tareas):
        tareas[indice_tarea_ajustado]['completada'] = True
        print(f'La tarea {indice_tarea} ha sido marcada como completada:')
        print(f'\n{ver_tareas(tareas)}')
    else:
        print('\n¡¡¡ÍNDICE DE TAREA INVÁLIDO!!!')
    return

# 5. Eliminar tareas completadas
def eliminar_tareas_completadas(tareas):
    for tarea in tareas:
        if tarea['completada']:
            tareas.remove(tarea)
    print('\n> Las tareas completadas han sido eliminadas')
    return