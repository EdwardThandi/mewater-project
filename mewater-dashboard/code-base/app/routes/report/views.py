from flask import Blueprint, render_template
# from flask_login import login_required, current_user
# from flask import current_app


# Create Blueprint
report_view = Blueprint('report_view',
                        __name__,
                        static_folder='static',
                        template_folder='templates')


@report_view.route('/report/')
# @login_required
def report():

    return render_template('report/report.html')
