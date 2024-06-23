import modulos_gestor
tareas = []

while True:
    print('\nMenú del gestor de Lista de Tareas:')
    print('\n1. Añadir tarea')
    print('2. Ver tareas')
    print('3. Actualizar tarea')
    print('4. Marcar como completada')
    print('5. Eliminar tareas completadas')
    print('6. Salir')

    eleccion = input('\nEscribe tu elección: ')

    if eleccion == '1':
        nombre_tarea = str(input('\nEscribe el nombre de la tarea que deseas añadir: '))
        modulos_gestor.añadir_tarea(tareas, nombre_tarea)
    elif eleccion == '2':
        modulos_gestor.ver_tareas(tareas)
    elif eleccion == '3':
        modulos_gestor.ver_tareas(tareas)
        indice_tarea = input('\nEscribe el número de la tarea que deseas actualizar: ')
        nuevo_nombre = input(f'\nEscribe el nuevo nombre de la tarea {indice_tarea}: ')
        modulos_gestor.actualizar_nombre_tarea(tareas, indice_tarea, nuevo_nombre)
    elif eleccion == '4':
        modulos_gestor.ver_tareas(tareas)
        indice_tarea = input('\nEscribe el número de la tarea para MARCAR COMO COMPLETADA: ')
        modulos_gestor.marcar_como_completada(indice_tarea, tareas)
    elif eleccion == '5':
        modulos_gestor.ver_tareas(tareas)
        limpiar = input('\n¿Realmente deseas eliminar las tareas completadas listadas?\nEscribe [S] para sí, [N] para no: ')
        if limpiar == 'S' or limpiar == 's':
            modulos_gestor.eliminar_tareas_completadas(tareas)
        elif limpiar == 'N' or limpiar == 'n':
            print('Limpieza cancelada')
        else:
            print('\nOpción inválida, operación cancelada')
    elif eleccion == '6':
        break

print('Programa finalizado')