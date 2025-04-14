from abc import ABC, abstractmethod

class IManager(ABC):
    @abstractmethod
    def add_task(self, text: str) -> None:
        """Добавляет новую задачу с заданным текстом.
        Args:
            text (str): Текст новой задачи.
        """
        pass

    @abstractmethod
    def mark_done(self, task_id: int) -> None:
        """Помечает задачу как завершенную по заданному идентификатору.
        Args:
            task_id (int): Идентификатор задачи, которую нужно пометить как завершенную.
        """
        pass

    @abstractmethod
    def edit_task(self, task_id: int, new_text: str) -> None:
        """Редактирует задачу, задавая новый текст.
        Args:
            task_id (int): Идентификатор задачи, которую нужно редактировать.
            new_text (str): Новый текст для задачи.
        """
        pass

    @abstractmethod
    def get_tasks(self) -> list:
        """Возвращает список всех текущих задач.
        Returns:
            list: Список задач.
        """
        pass

    @abstractmethod
    def delete_task(self, task_id: int) -> None:
        """Удаляет задачу по заданному идентификатору.
        Args:
            task_id (int): Идентификатор задачи, которую нужно удалить.
        """
        pass
