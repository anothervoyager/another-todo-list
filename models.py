from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TaskModel(Base):
    """
    Модель базы данных для задач.

    Атрибуты:
        task_id: Уникальный идентификатор задачи.
        text: Текст задачи.
        completed: Статус завершения задачи (True для завершенной, False для незавершенной).
    """
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    completed = Column(Boolean, default=False)