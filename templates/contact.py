import fastapi_tags as ft
import styles
import layout
import components


def render() -> ft.Html:
    """Render the contact page."""
    return layout.page(
        "Contact - Task Manager",
        components.page_header("Contact Us", "Contact"),
        components.info_card(
            ft.P(
                "Get in touch with us! We'd love to hear your feedback.",
                cls=styles.typography.text_with_margin
            ),
            components.input_with_button("message", "Enter your message", "Send Message", "/send-message", "#messages"),
            ft.Div(id="messages", cls=styles.layout.task_list),
            ft.P(
                "Other ways to reach us:",
                cls=styles.typography.text_semibold
            ),
            components.feature_list([
                "Email: hello@taskmanager.com",
                "Twitter: @taskmanager",
                "GitHub: taskmanager/issues"
            ])
        )
    ) 