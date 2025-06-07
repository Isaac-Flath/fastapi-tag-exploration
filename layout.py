import fastapi_tags as ft
import styles


def page(title: str, *content) -> ft.Html:
    """Base page layout with common HTML structure."""
    return ft.Html(
        ft.Head(
            ft.Title(title),
            ft.Script(src="https://unpkg.com/htmx.org@1.9.10"),
            ft.Script(src="https://cdn.tailwindcss.com")
        ),
        ft.Body(
            ft.Div(
                *content,
                cls=styles.layout.container
            ),
            cls=styles.layout.page
        )
    )


def header_with_nav(heading: str, nav_text: str, nav_href: str):
    """Header with title and navigation link."""
    return ft.Div(
        ft.H1(heading, cls=styles.typography.heading),
        ft.A(nav_text, href=nav_href, cls=styles.links.nav),
        cls=styles.layout.header
    ) 