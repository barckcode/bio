import reflex as rx
from components.rrss import rrss_component
from components.projects import project_component
from components.trusted import trusted_component


def header_view() -> rx.Component:
    return rx.box(
        rx.box(
            rx.image(
                src="/profile.jpg",
                class_name="rounded-full w-ful h-full",
                alt="Cristian photo"
            ),
            rx.box(
                rx.heading("Cristian Córdova"),
                rx.text("Indie Hacker & SRE"),
                rrss_component(),
                class_name="w-auto h-full"
            ),
            class_name="flex md:justify-center w-full h-40 py-6 gap-4"
        ),
        rx.box(
            "Me dedico a ayudar a empresas con todo lo referente a su infraestructura Cloud. También voy contando cómo creo productos digitales en mis diferentes redes sociales ya que apoyo mucho el movimiento #buildinpublic.",
            class_name="py-6 text-neutral-50 text-sm lg:text-base"
        ),
        trusted_component(),
        rx.box(
            rx.box(
                rx.heading("Proyectos"),
                class_name="text-center"
            ),
            project_component(),
        ),
        class_name="w-full h-auto mb-4"
    )
