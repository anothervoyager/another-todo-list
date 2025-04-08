from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from task import Task  # Импортируем ваш класс Task

# Настройки базы данных
DATABASE_URL = "postgresql://admin:admin@localhost:5432/cmd_todo_list"
# Замените <username>, <password>, и <dbname> на ваши значения

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class TaskModel(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    completed = Column(String, default='N')


# Создание всех таблиц в базе данных
Base.metadata.create_all(engine)


class DatabaseManager:
    """
    Класс для управления задачами в базе данных PostgreSQL.
    """

    def __init__(self):
        """
        Инициализация DatabaseManager и создание сессии.
        """
        self.session = Session()

    def add_task(self, text):
        """
        Добавить задачу в базу данных.

        :param text: Текст задачи
        :return: Идентификатор задачи
        """
        task_model = TaskModel(text=text, completed='N')
        self.session.add(task_model)
        self.session.commit()
        return task_model.task_id

    def mark_done(self, task_id):
        """
        Завершить задачу по идентификатору.

        :param task_id: Идентификатор задачи
        """
        task_model = self.session.query(TaskModel).filter(TaskModel.task_id == task_id).first()
        if task_model:
            task_model.completed = 'Y'
            self.session.commit()
        else:
            raise ValueError(f"Ошибка: Задача с ID {task_id} не найдена.")

    def edit_task(self, task_id, new_text):
        """
        Редактировать задачу.

        :param task_id: Идентификатор задачи
        :param new_text: Новый текст задачи
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

        :return: Список объектов Task
        """
        tasks = self.session.query(TaskModel).all()
        return [Task(task.task_id, task.text) for task in tasks]  # Создание объектов Task

    def delete_task(self, task_id):
        """
        Удалить задачу по идентификатору.

        :param task_id: Идентификатор задачи
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
        """
        self.session.close()
