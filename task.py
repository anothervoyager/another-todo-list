class Task:
    """
    Класс, представляющий задачу.

    Атрибуты:
        task_id: Уникальный идентификатор задачи.
        text: Текст задачи.
        done: Статус завершения задачи (по умолчанию - False).
    """

    def __init__(self, task_id, text):
        """
        Инициализация задачи.

        :param task_id: Идентификатор задачи.
        :param text: Текст задачи.
        """
        self.task_id = task_id
        self.text = text
        self.done = False

    def mark_done(self):
        """
        Отметить задачу как завершенную.

        Изменяет статус задачи на завершённый (done = True).
        """
        self.done = True

    def edit(self, new_text):
        """
        Редактировать текст задачи.

        :param new_text: Новый текст задачи.
        """
        self.text = new_text

    def __str__(self):
        """
        Возвращает строковое представление задачи.

        :return: Строковое представление задачи в формате:
                 [✓/✗] task_id: text.
        """
        status = "✓" if self.done else "✗"
        return f"[{status}] {self.task_id}: {self.text}"
