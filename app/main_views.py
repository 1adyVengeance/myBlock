from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def get_index():
    return render_template('templates/index.html')