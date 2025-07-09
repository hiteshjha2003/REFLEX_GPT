import reflex as rx
from .navbar import base_navbar

def base_layout(*args, **kwargs) -> rx.Component:
    """Navigation bar for the application."""
    return rx.container(
        base_navbar(),
        *args, **kwargs
    )
