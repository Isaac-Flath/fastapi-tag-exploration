import fastapi_tags as ft
import styles
import layout


def create_task_li(task: str, index: int):
    """Create a task list item with delete button."""
    return ft.Li(
        ft.Div(
            ft.Span(task, class_=styles.typography.text),
            ft.Button(
                "Delete",
                cls=styles.buttons.delete,
                **{
                    "hx-delete": f"/delete-task/{index}",
                    "hx-target": f"#task-{index}",
                    "hx-swap": "delete"
                }
            ),
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
        layout.header_with_nav("Task Manager", "About", "/about"),
        ft.Form(
            ft.Div(
                ft.Input(
                    type="text",
                    name="task",
                    placeholder="Enter task",
                    required=True,
                    cls=styles.forms.input
                ),
                ft.Button(
                    "Add Task",
                    type="submit",
                    cls=styles.buttons.primary_with_margin
                ),
                cls=styles.layout.form_group
            ),
            **{
                "hx-post": "/add-task",
                "hx-target": "#task-list",
                "hx-swap": "beforeend"
            }
        ),
        ft.Ul(*task_items, id="task-list", cls=styles.layout.task_list)
    )