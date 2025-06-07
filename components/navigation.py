import fastapi_tags as ft
import styles


def nav_bar(current_page: str = ""):
    """Reusable navigation bar component."""
    nav_items = [
        ("Home", "/"),
        ("About", "/about"), 
        ("Contact", "/contact")
    ]
    
    nav_links = []
    for i, (text, href) in enumerate(nav_items):
        if text.lower() == current_page.lower():
            nav_links.append(ft.Span(text, cls="font-semibold text-blue-600"))
        else:
            nav_links.append(ft.A(text, href=href, cls=styles.links.nav))
        
        if i < len(nav_items) - 1:
            nav_links.append(ft.Span(" | ", cls=styles.typography.text_muted))
    
    return ft.Div(*nav_links, cls="mb-4 text-center")


def page_header(title: str, current_page: str = ""):
    """Header with title and navigation bar."""
    return ft.Div(
        ft.H1(title, cls=styles.typography.heading),
        nav_bar(current_page),
        cls=styles.layout.header
    ) 