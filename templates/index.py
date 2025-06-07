import fastapi_tags as ft
import styles
import layout
import components


def create_task_li(task: str, index: int):
    """Create a task list item with delete button."""
    return ft.Li(
        ft.Div(
            ft.Span(task, class_=styles.typography.text),
            components.delete_button(index, "/delete-task", f"task-{index}"),
            cls=styles.layout.task_item
        ),
        id=f"task-{index}",
        cls=styles.components.task_item
    )


def render(tasks: list[str]) -> ft.Html:
    """Render the task manager page."""
    task_items = [create_task_li(task, i) for i, task in enumerate(tasks)]
    
    return layout.page(
        "Task Manager",
        components.page_header("Task Manager", "Home"),
        components.input_with_button("task", "Enter task", "Add Task", "/add-task", "#task-list"),
        ft.Ul(*task_items, id="task-list", cls=styles.layout.task_list)
    )