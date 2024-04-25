import reflex as rx
from enum import Enum


class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


class Color(Enum):
    PURPLE = "#6c62ff"


class TextColor(Enum):
    HEADER = "#F1F2F4"
    BODY = "#C3C7CB"


base = {
    "color": TextColor.BODY.value,
    rx.heading: {
        "color": TextColor.HEADER.value,
        "margin-bottom": "0.5rem"
    },
    rx.button: {
        "width": "100%",
        "height": "100%",
        "padding": Size.SMALL.value,
        "border_radius": Size.DEFAULT.value,
        "background_color": Color.PURPLE.value,
        "opacity": 1,
        "_hover": {
            "opacity": 0.8
        }
    }
}
