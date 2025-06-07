import fastapi_tags as ft
import styles
import layout


def render() -> ft.Html:
    """Render the about page."""
    return layout.page(
        "About - Task Manager",
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
        )
    ) 