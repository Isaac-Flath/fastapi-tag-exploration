import fastapi_tags as ft
import styles


def render() -> ft.Html:
    """Render the about page."""
    return ft.Html(
        ft.Head(
            ft.Title("About - Task Manager"),
            ft.Script(src="https://unpkg.com/htmx.org@1.9.10"),
            ft.Script(src="https://cdn.tailwindcss.com")
        ),
        ft.Body(
            ft.Div(
                ft.H1("About Task Manager", cls=styles.typography.heading),
                ft.Div(
                    ft.P(
                        "This is a simple task management application built with FastAPI and fastapi-tags.",
                        cls=styles.typography.text_with_margin
                    ),
                    ft.P(
                        "Features:",
                        cls=styles.typography.text_semibold
                    ),
                    ft.Ul(
                        ft.Li("Add new tasks", cls=styles.typography.text_muted),
                        ft.Li("Delete tasks with HTMX", cls=styles.typography.text_muted),
                        ft.Li("Responsive design with Tailwind CSS", cls=styles.typography.text_muted),
                        cls=styles.components.list
                    ),
                    ft.A(
                        "← Back to Tasks",
                        href="/",
                        cls=styles.buttons.primary_inline
                    ),
                    cls=styles.layout.content_card
                ),
                cls=styles.layout.container
            ),
            cls=styles.layout.page
        )
    ) 