from db_manager import DataBaseManager, Session
from console_manager import ConsoleManager
from imanager import IManager


class ToDoApp:
    def __init__(self, manager: IManager):
        self.manager = manager

    def add_task(self, *args, **kwargs):
        """Добавляет задачу, делегируя вызов менеджеру."""
        self.manager.add_task(*args, **kwargs)

    def mark_done(self, *args, **kwargs):
        """Помечает задачу как завершенную."""
        self.manager.mark_done(*args, **kwargs)

    def edit_task(self, *args, **kwargs):
        """Редактирует задачу."""
        self.manager.edit_task(*args, **kwargs)

    def get_tasks(self, *args, **kwargs):
        """Возвращает список всех задач."""
        return self.manager.get_tasks(*args, **kwargs)

    def delete_task(self, *args, **kwargs):
        """Удаляет задачу."""
        self.manager.delete_task(*args, **kwargs)

    def run(self):
        """Запускает взаимодействие с пользователем, обрабатывая команды."""
        try:
            while True:
                command = input("Введите команду (или 'exit' для выхода): ")
                if command.lower() == 'exit':
                    break
                self.execute_command(command)
        except KeyboardInterrupt:
            print("\nВыход из программы...")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

    def execute_command(self, command: str):
        """Обрабатывает команды пользователя."""
        parts = command.split()
        cmd = parts[0]

        try:
            if cmd == "add-task":
                self.add_task(" ".join(parts[1:]))
            elif cmd == "mark-done":
                self.mark_done(int(parts[1]))
            elif cmd == "edit-task":
                self.edit_task(int(parts[1]), " ".join(parts[2:]))
            elif cmd == "get-tasks":
                tasks = self.get_tasks()
                try:
                    for task in tasks:
                        print(task)
                except TypeError:
                    print("Ошибка: Не удалось перебрать задачи.")
            elif cmd == "delete-task":
                self.delete_task(int(parts[1]))
            else:
                print("Неизвестная команда.")
        except IndexError:
            print("Недостаточно аргументов для команды.")
        except ValueError:
            print("Неверный формат данных.")
        except Exception as e:
            print(f"Ошибка выполнения команды: {e}")


if __name__ == "__main__":
    session = Session()
    #тут нужно выбрать какой менеджер использовать
    db_manager = DataBaseManager(session)
    #console_manager = ConsoleManager()
    app = ToDoApp(db_manager)
    try:
        app.run()
    finally:
        session.close()