import reflex as rx

class AppConfig(rx.Config):
    pass


config = AppConfig(
    app_name="bio",
    next_compression=True,
    db_url="sqlite:///reflex.db",
    tailwind={
        "theme": {
            "screens": {
                'sm': '640px',
                'md': '768px',
                'lg': '1024px',
                'xl': '1200px',
            },
            "extend": {},
        },
        "plugins": []
    },
)
