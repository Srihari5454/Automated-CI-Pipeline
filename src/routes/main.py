from flask import Blueprint, render_template  # render_template not used

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():
    return "Hello, World!"