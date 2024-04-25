import reflex as rx


def company_logo(image: str) -> rx.Component:
    return rx.image(
        src=f"/{image}",
        class_name="rounded-lg w-8 h-8"
    )


def trusted_component() -> rx.Component:
    logos = [
        "bbva.jpeg",
        "telefonica.jpeg",
        "ovhgroup.jpeg",
        "glovo_app.jpeg",
        "metricool.jpeg",
        "paradigma_digital.jpeg",
        "zinkee.jpeg",
        "smartvel.jpeg",
        "nowo_tech.jpeg",
        "netmakers.jpeg"
    ]

    return rx.container(
        rx.heading(
            "TRUSTED BY ⏪⏩",
            size="1"
        ),
        rx.scroll_area(
            rx.box(
                *[
                    company_logo(image)
                    for image in logos
                ],
                class_name="flex gap-4"
            )
        ),
        class_name="w-full h-auto py-6 mb-4"
    )
