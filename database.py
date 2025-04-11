from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import TaskModel, Base  # Импортируем TaskModel из models.py
from consolemanager import ConsoleManager  # Импортируем ваш класс Task

# Конфигурация базы данных
DATABASE_URL = "postgresql://admin:admin@localhost:5432/cmd_todo_list"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# Создание всех таблиц в базе данных
Base.metadata.create_all(engine)

class DatabaseManager:
    """
    Класс для управления задачами в базе данных PostgreSQL.

    Обеспечивает операции добавления, завершения, редактирования, получения и удаления задач.
    """

    def __init__(self, session):
        """
        Инициализация DatabaseManager и создание сессии.

        :param session: Сессия для выполнения операций с базой данных.
        """
        self.session = session

    def add_task(self, text):
        """
        Добавить задачу в базу данных.

        :param text: Текст задачи.
        :return: Идентификатор добавленной задачи.
        """
        task_model = TaskModel(text=text, completed=False)  # Установлено значение по умолчанию
        self.session.add(task_model)
        self.session.commit()
        return task_model.task_id

    def mark_done(self, task_id):
        """
        Завершить задачу по идентификатору.

        :param task_id: Идентификатор задачи, которую необходимо завершить.
        :raises ValueError: Если задача с заданным ID не найдена.
        """
        task_model = self.session.query(TaskModel).filter(TaskModel.task_id == task_id).first()
        if task_model:
            task_model.completed = True  # Установка статуса завершенной задачи
            self.session.commit()
        else:
            raise ValueError(f"Ошибка: Задача с ID {task_id} не найдена.")

    def edit_task(self, task_id, new_text):
        """
        Редактировать задачу.

        :param task_id: Идентификатор задачи, которую необходимо редактировать.
        :param new_text: Новый текст задачи.
        :raises ValueError: Если задача с заданным ID не найдена.
        """
        task_model = self.session.query(TaskModel).filter(TaskModel.task_id == task_id).first()
        if task_model:
            task_model.text = new_text
            self.session.commit()
        else:
            raise ValueError(f"Ошибка: Задача с ID {task_id} не найдена.")

    def get_tasks(self):
        """
        Получить список всех задач.

        :return: Список объектов Task, содержащий текст и идентификатор каждой задачи.
        """
        tasks = self.session.query(TaskModel).all()
        return [ConsoleManager(task.task_id, task.text) for task in tasks]  # Создание объектов Task

    def delete_task(self, task_id):
        """
        Удалить задачу по идентификатору.

        :param task_id: Идентификатор задачи, которую необходимо удалить.
        :raises ValueError: Если задача с заданным ID не найдена.
        """
        task_model = self.session.query(TaskModel).filter(TaskModel.task_id == task_id).first()
        if task_model:
            self.session.delete(task_model)
            self.session.commit()
        else:
            raise ValueError(f"Ошибка: Задача с ID {task_id} не найдена.")

    def close(self):
        """
        Закрыть сессию.

        Завершает работу с текущей сессией и освобождает ресурсы.
        """
        self.session.close()
