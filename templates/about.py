import fastapi_tags as ft
import styles
import layout
import components


def render() -> ft.Html:
    """Render the about page."""
    return layout.page(
        "About - Task Manager",
        components.page_header("About Task Manager", "About"),
        components.info_card(
            ft.P(
                "This is a simple task management application built with FastAPI and fastapi-tags.",
                cls=styles.typography.text_with_margin
            ),
            ft.P(
                "Features:",
                cls=styles.typography.text_semibold
            ),
            components.feature_list([
                "Add new tasks",
                "Delete tasks with HTMX", 
                "Responsive design with Tailwind CSS"
            ])
        )
    ) 