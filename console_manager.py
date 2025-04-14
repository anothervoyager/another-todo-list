from imanager import IManager
from task import Task


class ConsoleManager(IManager):
    def __init__(self) -> None:
        """
        Инициализация менеджера задач.
        """
        self.tasks = {}
        self.next_id = 1

    def add_task(self, text: str) -> int:
        """
        Добавить задачу.

        :param text: Текст задачи
        :return: Идентификатор задачи
        """
        task = Task(self.next_id, text)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task.task_id

    def mark_done(self, task_id: int) -> None:
        """
        Завершить задачу по идентификатору.
        :param task_id: Идентификатор задачи
        """
        if task_id in self.tasks:
            self.tasks[task_id].mark_done()
        else:
            print(f"Ошибка: Задача с ID {task_id} не найдена.")

    def edit_task(self, task_id: int, new_text: str) -> None:
        """
        Редактировать задачу.
        :param task_id: Идентификатор задачи
        :param new_text: Новый текст задачи
        """
        if task_id in self.tasks:
            self.tasks[task_id].edit(new_text)
        else:
            print(f"Ошибка: Задача с ID {task_id} не найдена.")

    def get_tasks(self) -> None:
        """
        Получить список всех задач.
        """
        if not self.tasks:
            print("Нет задач.")
            return
        for task in self.tasks.values():
            print(task)

    def delete_task(self, task_id: int) -> None:
        """
        Удалить задачу по идентификатору.
        :param task_id: Идентификатор задачи
        """
        if task_id in self.tasks:
            del self.tasks[task_id]
        else:
            print(f"Ошибка: Задача с ID {task_id} не найдена.")
