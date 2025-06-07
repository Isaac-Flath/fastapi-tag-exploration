import fastapi_tags as ft


def create_task_li(task: str, index: int):
    """Create a task list item with delete button."""
    return ft.Li(
        task,
        ft.Button(
            "Delete",
            **{
                "hx-delete": f"/delete-task/{index}",
                "hx-target": f"#task-{index}",
                "hx-swap": "delete"
            }
        ),
        id=f"task-{index}"
    )


def render(tasks: list[str]) -> ft.Html:
    """Render the task manager page."""
    task_items = [create_task_li(task, i) for i, task in enumerate(tasks)]
    
    return ft.Html(
        ft.Head(
            ft.Title("Task Manager"),
            ft.Script(src="https://unpkg.com/htmx.org@1.9.10")
        ),
        ft.Body(
            ft.H1("Task Manager"),
            ft.Form(
                ft.Input(type="text", name="task", placeholder="Enter task", required=True),
                ft.Button("Add Task", type="submit"),
                **{
                    "hx-post": "/add-task",
                    "hx-target": "#task-list",
                    "hx-swap": "beforeend"
                }
            ),
            ft.Ul(*task_items, id="task-list")
        )
    ) 