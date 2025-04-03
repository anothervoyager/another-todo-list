from task import Task  # Импортируем Task из task.py

class TaskManager:
    """
    Класс для управления задачами.
    """

    def __init__(self):
        """
        Инициализация менеджера задач.
        """
        self.tasks = {}
        self.next_id = 1

    def add_task(self, text):
        """
        Добавить задачу.

        :param text: Текст задачи
        :return: Идентификатор задачи
        """
        task = Task(self.next_id, text)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task.task_id

    def mark_done(self, task_id):
        """
        Завершить задачу по идентификатору.

        :param task_id: Идентификатор задачи
        """
        if task_id in self.tasks:
            self.tasks[task_id].mark_done()
        else:
            print(f"Ошибка: Задача с ID {task_id} не найдена.")

    def edit_task(self, task_id, new_text):
        """
        Редактировать задачу.

        :param task_id: Идентификатор задачи
        :param new_text: Новый текст задачи
        """
        if task_id in self.tasks:
            self.tasks[task_id].edit(new_text)
        else:
            print(f"Ошибка: Задача с ID {task_id} не найдена.")

    def get_tasks(self):
        """
        Получить список всех задач.
        """
        if not self.tasks:
            print("Нет задач.")
            return
        for task in self.tasks.values():
            print(task)

    def delete_task(self, task_id):
        """
        Удалить задачу по идентификатору.

        :param task_id: Идентификатор задачи
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            print(f"Ошибка: Задача с ID {task_id} не найдена.")
