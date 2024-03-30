from flask import Blueprint, redirect, url_for

index_view = Blueprint('index_view', __name__)

@index_view.route('/')
def index():

    return redirect(url_for('dashboard_view.dashboard'))