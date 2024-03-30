from flask import Blueprint, render_template
# from flask_login import login_required
from app.aws import aws_functions
from datetime import datetime, date

# Create Blueprint
dashboard_view = Blueprint('dashboard_view',
                           __name__,
                           static_folder='static',
                           template_folder='templates')


@dashboard_view.route('/dashboard/')
# @login_required
def dashboard():

    current_date = date.today()

    current_leakage_info = int(aws_functions.get_leakage_info())

    current_consumption_info = aws_functions.get_consumption_info()
    current_consumption = int(
        current_consumption_info['outlet_1']) + int(current_consumption_info['outlet_2'])
    outlets = list(current_consumption_info.keys())
    outlets_data = list(current_consumption_info.values())

    hourly_consumption = aws_functions.get_hourly_usage()
    hourly_consumption_dict = {}
    for i in hourly_consumption:
        time = int(i['time'])
        parsed_time = datetime.fromtimestamp(time).hour
        total_volume = int(i['outlet1_volume']) + int(i['outlet2_volume'])

        hourly_consumption_dict[parsed_time] = total_volume

    hours = list(hourly_consumption_dict.keys())
    hour_consumption = list(hourly_consumption_dict.values())

    return render_template('dashboard/dashboard.html',
                           current_date=current_date,
                           current_leakage_info=current_leakage_info,
                           current_consumption=current_consumption,
                           current_consumption_info=current_consumption_info,
                           outlets=outlets,
                           outlets_data=outlets_data,
                           hours=hours,
                           hour_consumption=hour_consumption,)
