import reflex as rx
from components.rrss import rrss_component

def header_view() -> rx.Component:
    return rx.box(
        rx.box(
            rx.image(
                src="/profile.jpg",
                class_name="rounded-full w-ful h-full"
            ),
            rx.box(
                rx.heading(
                    "Cristian Córdova",
                    margin_bottom="0.5rem"
                ),
                rx.text("Indie Hacker"),
                rrss_component(),
                class_name="w-full h-full"
            ),
            class_name="flex h-40 p-6 gap-4"
        ),
        class_name="bg-blue-950 w-full h-screen"
    )
