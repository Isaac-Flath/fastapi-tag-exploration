import fastapi_tags as ft
import styles


def input_with_button(input_name: str, input_placeholder: str, button_text: str, 
                     hx_post: str, hx_target: str, hx_swap: str = "beforeend"):
    """Reusable form with input and button."""
    return ft.Form(
        ft.Div(
            ft.Input(
                type="text",
                name=input_name,
                placeholder=input_placeholder,
                required=True,
                cls=styles.forms.input
            ),
            ft.Button(
                button_text,
                type="submit",
                cls=styles.buttons.primary_with_margin
            ),
            cls=styles.layout.form_group
        ),
        **{
            "hx-post": hx_post,
            "hx-target": hx_target,
            "hx-swap": hx_swap
        }
    ) 