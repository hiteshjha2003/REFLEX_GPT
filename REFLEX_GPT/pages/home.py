import reflex as rx

from rxconfig import config

from REFLEX_GPT import ui




def home_page() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex GPT", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )
