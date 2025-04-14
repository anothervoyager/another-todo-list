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
    def __init__(self, session):
        self.session = session

    def add_task(self, text):
        try:
            new_task = TaskModel(text=text)
            self.session.add(new_task)
            self.session.commit()
            return new_task.task_id
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Ошибка при добавлении задачи: {e}")

    def mark_done(self, task_id):
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

    def edit_task(self, task_id, new_text):
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

    def get_tasks(self):
        try:
            tasks = self.session.query(TaskModel).all()
            return [(task.task_id, task.text, task.completed) for task in tasks]
        except SQLAlchemyError as e:
            print(f"Ошибка при получении задач: {e}")
            return []

    def delete_task(self, task_id):
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
