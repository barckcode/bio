import reflex as rx

class AppConfig(rx.Config):
    pass


config = AppConfig(
    app_name="bio",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
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
