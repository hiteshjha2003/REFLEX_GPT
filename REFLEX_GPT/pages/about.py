import reflex as rx

from rxconfig import config
from REFLEX_GPT import ui


def about_us_page() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex-GPT!", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )



