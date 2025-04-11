class CommandStrategy:
    def execute(self, db_manager, *args):
        raise NotImplementedError("Must implement execute method")

class AddTaskCommand(CommandStrategy):
    def execute(self, db_manager, task_text):
        return db_manager.add_task(task_text)

class MarkDoneCommand(CommandStrategy):
    def execute(self, db_manager, task_id):
        db_manager.mark_done(task_id)

class EditTaskCommand(CommandStrategy):
    def execute(self, db_manager, task_id, new_text):
        db_manager.edit_task(task_id, new_text)

class GetTasksCommand(CommandStrategy):
    def execute(self, db_manager):
        return db_manager.get_tasks()

class DeleteTaskCommand(CommandStrategy):
    def execute(self, db_manager, task_id):
        db_manager.delete_task(task_id)
