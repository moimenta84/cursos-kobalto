"""
Proyecto CLI - Método delete_task
Módulo: PYTHON
Fecha: 2026-11-20 10:45

"""
def delete_task(self, index):
    if index < 1 or index > len(self.tasks):
        print("Índice inválido")
        return

    task = self.tasks.pop(index - 1)
    print(f"Tarea eliminada: {task.title}")