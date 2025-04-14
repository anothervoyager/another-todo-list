class Task:
    """
    Класс, представляющий задачу.
    """

    def __init__(self, task_id, text):
        """
        Инициализация задачи.

        :param task_id: Идентификатор задачи
        :param text: Текст задачи
        """
        self.task_id = task_id
        self.text = text
        self.done = False

    def mark_done(self):
        """
        Отметить задачу как завершенную.
        """
        self.done = True

    def edit(self, new_text):
        """
        Редактировать текст задачи.

        :param new_text: Новый текст задачи
        """
        self.text = new_text

    def __str__(self):
        """
        Возвращает строковое представление задачи.

        :return: Строковое представление задачи
        """
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.task_id}: {self.text}"