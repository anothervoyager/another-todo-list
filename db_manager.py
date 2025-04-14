from imanager import IManager
from models import TaskModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "postgresql://admin:admin@localhost:5432/cmd_todo_list"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


class DataBaseManager(IManager):
    def __init__(self, session: Session) -> None:
        """Инициализирует DataBaseManager с текущей сессией.
        Args:
            session (Session): Объект сессии SQLAlchemy для взаимодействия с базой данных.
        """
        self.session = session

    def add_task(self, text: str) -> int:
        """Добавляет новую задачу в базу данных.

        Args:
            text (str): Текст задачи, которую необходимо добавить.
        Returns:
            int: Идентификатор добавленной задачи, если все прошло успешно.
        """
        try:
            new_task = TaskModel(text=text)
            self.session.add(new_task)
            self.session.commit()
            return new_task.task_id
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Ошибка при добавлении задачи: {e}")
            return -1  # Возвращаем -1 в случае ошибки

    def mark_done(self, task_id: int) -> None:
        """Помечает задачу как выполненную по её идентификатору.
        Args:
            task_id (int): Идентификатор задачи, которую нужно пометить как завершенную.
        """
        try:
            task = self.session.query(TaskModel).get(task_id)
            if task:
                task.completed = True
                self.session.commit()
            else:
                print("Задача не найдена.")
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Ошибка при завершении задачи: {e}")

    def edit_task(self, task_id: int, new_text: str) -> None:
        """Редактирует текст задачи по её идентификатору.
        Args:
            task_id (int): Идентификатор задачи, которую необходимо редактировать.
            new_text (str): Новый текст для задачи.
        """
        try:
            task = self.session.query(TaskModel).get(task_id)
            if task:
                task.text = new_text
                self.session.commit()
            else:
                print("Задача не найдена.")
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Ошибка при редактировании задачи: {e}")

    def get_tasks(self) -> list:
        """Получает список всех задач из базы данных.
        Returns:
            list: Список кортежей, содержащих идентификатор задачи, её текст и статус выполнения.
        """
        try:
            tasks = self.session.query(TaskModel).all()
            return [(task.task_id, task.text, task.completed) for task in tasks]
        except SQLAlchemyError as e:
            print(f"Ошибка при получении задач: {e}")
            return []

    def delete_task(self, task_id: int) -> None:
        """Удаляет задачу из базы данных по её идентификатору.
        Args:
            task_id (int): Идентификатор задачи, которую нужно удалить.
        """
        try:
            task = self.session.query(TaskModel).get(task_id)
            if task:
                self.session.delete(task)
                self.session.commit()
            else:
                print("Задача не найдена.")
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Ошибка при удалении задачи: {e}")
