import fastapi_tags as ft
import styles


def delete_button(index: int, endpoint: str, target_id: str):
    """Reusable delete button with HTMX."""
    return ft.Button(
        "Delete",
        cls=styles.buttons.delete,
        **{
            "hx-delete": f"{endpoint}/{index}",
            "hx-target": f"#{target_id}",
            "hx-swap": "delete"
        }
    )


def nav_button(text: str, href: str):
    """Reusable navigation button."""
    return ft.A(text, href=href, cls=styles.buttons.primary_inline) 