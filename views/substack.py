import reflex as rx


def subtack_view() -> rx.Component:
    return rx.container(
        rx.box(
            rx.box(
                rx.heading("Newsletter"),
                class_name="text-center"
            ),
            class_name="mb-4"
        ),
        rx.html(
            '<iframe src="https://helmcode.substack.com/embed" width="100%" height="320" style="border-radius: 0.5rem;" frameborder="0" scrolling="no"></iframe>'
        ),
        class_name="w-full h-auto py-6 mb-4"
    )
