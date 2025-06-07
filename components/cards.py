import fastapi_tags as ft
import styles


def info_card(*content):
    """Reusable info card component."""
    return ft.Div(*content, cls=styles.layout.content_card)


def feature_list(items: list[str]):
    """Reusable feature list component."""
    return ft.Ul(
        *[ft.Li(item, cls=styles.typography.text_muted) for item in items],
        cls=styles.components.list
    ) 