from database import DatabaseManager  # Импортируем DatabaseManager из database.py


class TodoApp:
    """
    Основной класс приложения Todo, отвечающий за управление задачами.
    """

    def __init__(self):
        """
        Инициализирует объект базы данных, создавая экземпляр DatabaseManager.
        """
        self.db_manager = DatabaseManager()

    def run(self):
        """
        Запускает основной цикл приложения, ожидая ввод команд от пользователя.

        Ввод команд:
        - add-task: добавить задачу
        - mark-done: отметить задачу как завершенную
        - edit-task: редактировать существующую задачу
        - get-tasks: получить список всех задач
        - delete-task: удалить задачу
        - exit: завершает работу приложения
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

        :param command: Строка команды, введенная пользователем.
        """
        try:
            match command.split(maxsplit=1):
                case ["add-task"]:
                    task_text = input("Введите текст задачи: ")
                    task_id = self.db_manager.add_task(task_text)
                    print(f"Задача добавлена с ID {task_id}")

                case ["mark-done", task_id_text]:
                    task_id = int(task_id_text)
                    self.db_manager.mark_done(task_id)
                    print(f"Задача с ID {task_id} отмечена как завершенная.")

                case ["edit-task", task_id_text]:
                    task_id = int(task_id_text)
                    new_text = input("Введите новый текст задачи: ")
                    self.db_manager.edit_task(task_id, new_text)
                    print(f"Задача с ID {task_id} обновлена.")

                case ["get-tasks"]:
                    tasks = self.db_manager.get_tasks()
                    print("Все задачи:")
                    for task in tasks:
                        print(task)

                case ["delete-task", task_id_text]:
                    task_id = int(task_id_text)
                    self.db_manager.delete_task(task_id)
                    print(f"Задача с ID {task_id} удалена.")

                case _:
                    print("Неизвестная команда")

        except (IndexError, ValueError) as e:
            print(f"Ошибка ввода: {e}")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

        finally:
            # Закрывает соединение с базой данных
            self.db_manager.close()


if __name__ == "__main__":
    app = TodoApp()
    app.run()
