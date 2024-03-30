from flask import Blueprint, render_template
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

    current_leakage_info = 0

    current_consumption_info = {
        "outlet_1": 0,
        "outlet_2": 0
    }
    current_consumption = 0
    outlets = list(current_consumption_info.keys())
    outlets_data = list(current_consumption_info.values())

    # hourly_consumption = []
    hourly_consumption_dict = {
        "0": "0",
        "1": "0",
    }
    # for i in hourly_consumption:
    #     time = int(i['time'])
    #     parsed_time = datetime.fromtimestamp(time).hour
    #     total_volume = int(i['outlet1_volume']) + int(i['outlet2_volume'])

    #     hourly_consumption_dict[parsed_time] = total_volume

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
