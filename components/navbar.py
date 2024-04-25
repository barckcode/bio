import reflex as rx


def navbar_component() -> rx.Component:
    return rx.box(
        rx.box(
            rx.avatar(src="/logo_transparent.png", fallback="HELMCODE", size="5"),
            class_name="w-3/12"
        ),
        rx.box(
            rx.link(
                rx.button("Agenda una reunión"),
                href="https://calendly.com/helmcode/work",
                is_external=True
            ),
            class_name="w-3/6 h-2/3"
        ),
        class_name="flex items-center justify-between w-full h-16",
    )
