import reflex as rx


def rrss_component() -> rx.Component:
    return rx.box(
        rx.link(
            rx.icon("github"),
            href="https://github.com/barckcode",
            is_external=True
        ),
        rx.link(
            rx.icon("twitter"),
            href="https://twitter.com/barckcode",
            is_external=True
        ),
        rx.link(
            rx.icon("linkedin"),
            href="https://www.linkedin.com/in/helmcode/",
            is_external=True
        ),
        rx.link(
            rx.icon("bookmark"),
            href="https://helmcode.substack.com/",
            is_external=True
        ),
        class_name="flex w-full h-auto py-4 gap-4"
    )
