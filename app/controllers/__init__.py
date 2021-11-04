from flask import Flask
from app.controllers.posts_controller import posts_controller

def init_app(app: Flask):
    posts_controller(app)

    return app