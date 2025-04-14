from abc import ABC, abstractmethod

class IManager:
    @abstractmethod
    def add_task(self, text):
        pass
    @abstractmethod
    def mark_done(self, task_id):
        pass
    @abstractmethod
    def edit_task(self, task_id, new_text):
        pass
    @abstractmethod
    def get_tasks(self):
        pass
    @abstractmethod
    def delete_task(self, task_id):
        pass

