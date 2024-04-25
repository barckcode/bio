import reflex as rx
from styles.index import base
from components.navbar import navbar_component
from views.header import header_view
from views.substack import subtack_view


def index():
    return rx.container(
        navbar_component(),
        header_view(),
        subtack_view(),
        class_name="bg-blue-950 w-full h-full px-6"
    )


app = rx.App(
    style=base
)
app.add_page(index)
