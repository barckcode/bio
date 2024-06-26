import reflex as rx


def project_card(image: str, title: str, url: str, description: str, revenue: str, info: str) -> rx.Component:
    return rx.box(
        rx.link(
            rx.image(
                src=f"/{image}",
                class_name="rounded-lg",
                alt="Project logo"
            ),
            href=url,
            is_external=True,
            class_name="w-1/2 md:w-24 lg:w-32 h-full md:h-24 lg:h-32"
        ),
        rx.box(
            rx.link(
                rx.heading(
                    title,
                    size="4"
                ),
                href=url,
                is_external=True
            ),
            rx.text(
                description,
                size="3"
            ),
            rx.box(
                rx.text(
                    revenue,
                    size="1",
                    weight="bold"
                ),
                rx.text(
                    info,
                    size="1",
                    weight="bold"
                ),
                class_name="flex md:justify-between py-2 gap-4"
            ),
            class_name="w-auto h-full"
        ),
        class_name="flex md:flex-col md:items-center py-6 gap-4 border-b border-blue-200 md:border-0"
    )


def project_component() -> rx.Component:
    projects = [
        (
            "helmcode.png",
            "Helmcode",
            "https://helmcode.com/",
            "DevOps as a Service para Startups",
            "+180K€ ARR",
            "+20 empresas",
        ),
        (
            "andulia.jpg",
            "Andulia",
            "https://andulia.com/",
            "Asistente de viajes con IA en WhatsApp",
            "0€",
            "+200 usuarios"
        )
    ]

    return rx.container(
        *[
            project_card(image, title, url, description, revenue, info)
            for image, title, url, description, revenue, info in projects
        ],
        class_name="projects"
    )
