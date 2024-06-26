import reflex as rx
from styles.index import base
from components.navbar import navbar_component
from components.footer import footer_component
from views.header import header_view
from views.substack import subtack_view


def index():
    return rx.container(
        rx.box(
            navbar_component(),
            header_view(),
            subtack_view(),
            footer_component(),
            class_name="max-w-screen-lg w-full h-full px-6"
        ),
        class_name="bg-blue-950 w-full h-full md:text-center"
    )


app = rx.App(
    style=base,
    stylesheets=["/styles.css"],
    html_lang="es"
)
app.add_page(index)
