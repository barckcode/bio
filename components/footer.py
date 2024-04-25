import reflex as rx


def footer_component() -> rx.Component:
    return rx.box(
        rx.heading(
            "©2024 Helmcode",
            size="1"
        ),
        rx.heading(
            "De Canarias para el 🌎",
            size="1"
        ),
        class_name="w-full h-16 py-4 text-center"
    )
