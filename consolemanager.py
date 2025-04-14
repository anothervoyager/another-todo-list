class ConsoleManager:
    """
    Класс, представляющий задачу.

    Атрибуты:
        task_id: Уникальный идентификатор задачи.
        text: Текст задачи.
        done: Статус завершения задачи.
    """

    def __init__(self, task_id, text, done=False):
        """
        Инициализация задачи.

        :param task_id: Идентификатор задачи.
        :param text: Текст задачи.
        :param done: Статус завершенности задачи (по умолчанию - False).
        """
        self.task_id = task_id
        self.text = text
        self.done = done  # Устанавливаем статус завершенности при инициализации

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
