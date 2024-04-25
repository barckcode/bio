import reflex as rx


def company_logo(image: str) -> rx.Component:
    return rx.image(
        src=f"/{image}",
        class_name="rounded-lg w-8 lg:w-14 h-8 lg:h-14"
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
        rx.box(
            rx.mobile_and_tablet(
                rx.heading(
                    "TRUSTED BY ⏪⏩",
                    size="1"
                ),
            ),
            rx.tablet_and_desktop(
                rx.heading(
                    "TRUSTED BY ⏪⏩",
                    size="2"
                ),
            ),
            class_name="text-center lg:mb-4"
        ),
        rx.scroll_area(
            rx.box(
                *[
                    company_logo(image)
                    for image in logos
                ],
                class_name="flex md:justify-between gap-4"
            )
        ),
        class_name="w-full h-auto py-6 mb-4"
    )
