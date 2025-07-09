
import reflex as rx

from rxconfig import config


from .import ui 
from .import pages



class State(rx.State):
    """The app state."""




app = rx.App()
app.add_page(pages.home_page, route="/")
app.add_page(pages.about_us_page, route="/about")

