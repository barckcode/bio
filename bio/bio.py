import reflex as rx
from styles.index import base
from components.navbar import navbar_component
from views.header import header_view


def index():
    return rx.container(
        navbar_component(),
        header_view(),
    )


app = rx.App(
    style=base
)
app.add_page(index)
