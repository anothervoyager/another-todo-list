from task_manager import TaskManager  # Импортируем TaskManager из task_manager.py


class TodoApp:
    """
    Основной класс приложения
    """

    def __init__(self):
        """
        Инициализируем объект планировщика
        """
        self.task_manager = TaskManager()

    def run(self):
        """
        Запускает основной цикл приложения, ожидая ввод команд от пользователя.

        В этом методе происходит:
        - Запрос ввода команды от пользователя.
        - Обработка введенной команды и выполнение соответствующих действий.
        - Позволяет завершить выполнение программы при вводе команды "exit".
        - Обрабатывает исключение KeyboardInterrupt для корректного завершения приложения
          при нажатии Ctrl+C.

        Команды, которые могут быть введены:
        - 'add-task': Добавить новую задачу.
        - 'mark-done': Завершить задачу по ее идентификатору.
        - 'edit-task': Изменить текст существующей задачи.
        - 'get-tasks': Получить список всех задач.
        - 'delete-task': Удалить задачу по ее идентификатору.
        - 'exit': Завершить выполнение программы.
        """
        while True:
            try:
                command = input("Введите команду (add-task, mark-done, edit-task, get-tasks, delete-task, exit): ")

                match command:
                    case "exit":
                        print("Завершение программы...")
                        break
                    case _:
                        self.process_command(command)

            except KeyboardInterrupt:
                print("\nЗавершение программы...")
                break

    def process_command(self, command):
        """
        Обрабатывает введенную команду и выполняет соответствующее действие.

        :param command: Строка команды, введенная пользователем. Поддерживаемые команды:
            - add-task: добавить новую задачу.
            - mark-done <task_id>: отметить задачу как завершенную.
            - edit-task <task_id>: изменить текст задачи.
            - get-tasks: вывести список всех задач.
            - delete-task <task_id>: удалить задачу по идентификатору.

        Обрабатывает ошибки ввода, такие как неверные идентификаторы задач или неправильно введенные команды.
        """
        try:
            match command.split(maxsplit=1):
                case ["add-task"]:
                    task_text = input("Введите текст задачи: ")
                    task_id = self.task_manager.add_task(task_text)
                    print(f"Задача добавлена с ID {task_id}")

                case ["mark-done", task_id_text]:
                    task_id = int(task_id_text)
                    self.task_manager.mark_done(task_id)

                case ["edit-task", task_id_text]:
                    task_id = int(task_id_text)
                    new_text = input("Введите новый текст задачи: ")
                    self.task_manager.edit_task(task_id, new_text)

                case ["get-tasks"]:
                    self.task_manager.get_tasks()

                case ["delete-task", task_id_text]:
                    task_id = int(task_id_text)
                    self.task_manager.delete_task(task_id)

                case _:
                    print("Неизвестная команда")

        except (IndexError, ValueError) as e:
            print(f"Ошибка ввода: {e}")


if __name__ == "__main__":
    app = TodoApp()
    app.run()
