from sqlalchemy.orm import sessionmaker
from database import DatabaseManager, engine  # Импортируем DatabaseManager и engine
from commands import (  # Импортируем стратегии команд
    AddTaskCommand,
    MarkDoneCommand,
    EditTaskCommand,
    GetTasksCommand,
    DeleteTaskCommand,
)

class TodoApp:
    """
    Основной класс приложения Todo, отвечающий за управление задачами.

    Этот класс предоставляет пользовательский интерфейс для управления задачами,
    включая добавление, удаление, редактирование и получение задач.
    """

    def __init__(self, db_manager):
        """
        Инициализирует приложение с переданным объектом DatabaseManager.

        :param db_manager: Экземпляр DatabaseManager для взаимодействия с базой данных.
        """
        self.db_manager = db_manager  # Сохраняем экземпляр DatabaseManager
        self.command_map = {
            "add-task": AddTaskCommand(),   # Команда добавления задачи
            "mark-done": MarkDoneCommand(),  # Команда отметки задачи как завершенной
            "edit-task": EditTaskCommand(),  # Команда редактирования задачи
            "get-tasks": GetTasksCommand(),   # Команда получения всех задач
            "delete-task": DeleteTaskCommand(), # Команда удаления задачи
        }

    def run(self):
        """
        Запускает основной цикл приложения, ожидая ввод команд от пользователя.

        Метод предоставляет пользователю интерактивный интерфейс,
        где он может вводить команды для управления задачами.
        """
        while True:
            try:
                command = input("Введите команду (add-task, mark-done, edit-task, get-tasks, delete-task, exit): ")

                if command == "exit":
                    print("Завершение программы...")
                    break
                else:
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
            parts = command.split(maxsplit=1)
            action = parts[0]
            args = parts[1] if len(parts) > 1 else ""

            if action in self.command_map:
                command_strategy = self.command_map[action]

                if action == "add-task":
                    task_text = input("Введите текст задачи: ")
                    task_id = command_strategy.execute(self.db_manager, task_text)
                    print(f"Задача добавлена с ID {task_id}")

                elif action == "mark-done":
                    task_id = int(args)
                    command_strategy.execute(self.db_manager, task_id)
                    print(f"Задача с ID {task_id} отмечена как завершенная.")

                elif action == "edit-task":
                    task_id = int(args)
                    new_text = input("Введите новый текст задачи: ")
                    command_strategy.execute(self.db_manager, task_id, new_text)
                    print(f"Задача с ID {task_id} обновлена.")

                elif action == "get-tasks":
                    tasks = command_strategy.execute(self.db_manager)
                    print("Все задачи:")

                    for task in tasks:
                        print(task)

                elif action == "delete-task":
                    task_id = int(args)
                    command_strategy.execute(self.db_manager, task_id)
                    print(f"Задача с ID {task_id} удалена.")

            else:
                print("Неизвестная команда")

        except (IndexError, ValueError) as e:
            print(f"Ошибка ввода: {e}")

        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def close(self):
        """
        Закрывает соединение с базой данных.

        Вызывается при завершении работы приложения для корректного
        освобождения ресурсов, связанных с базой данных.
        """
        self.db_manager.close()  # Закрываем соединение с базой данных


if __name__ == "__main__":
    # Создаем сессию
    session = sessionmaker(bind=engine)()
    # Создаем экземпляр DatabaseManager
    db_manager = DatabaseManager(session)
    # Передаем экземпляр DatabaseManager в TodoApp
    app = TodoApp(db_manager)

    try:
        app.run()
    finally:
        app.close()  # Закрываем соединение с базой данных при завершении программы
