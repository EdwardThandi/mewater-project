from flask import Blueprint, render_template
from datetime import datetime, date
from app import db
from app.models import ApartmentWaterConsumption
from pprint import pprint

# Create Blueprint
dashboard_view = Blueprint('dashboard_view',
                           __name__,
                           static_folder='static',
                           template_folder='templates')


@dashboard_view.route('/dashboard/')
# @login_required
def dashboard():
    
    apartment_data = db.session.query(ApartmentWaterConsumption).all()
    print(apartment_data)
    
    apartment_data_dict = {}
    for i in apartment_data:
        apartment_data_dict[i.apartment_name] = {
            "Week 0": i.instance_1,
            "Week 1": i.instance_2,
            "Week 2": i.instance_3,
            "Week 3": i.instance_4,
            "Week 4": i.instance_5,
            "Week 5": i.instance_6
        }
        
    pprint(apartment_data_dict)
    
    apartment_names = list(apartment_data_dict.keys())
    print(apartment_names)
    
    weeks = ["Week 0",
            "Week 1",
            "Week 2",
            "Week 3",
            "Week 4",
            "Week 5",
            ]
    
    apartment1 = list(apartment_data_dict['A'].values())
    apartment2 = list(apartment_data_dict['B'].values())
    apartment3 = list(apartment_data_dict['C'].values())
    apartment4 = list(apartment_data_dict['D'].values())
    apartment5 = list(apartment_data_dict['E'].values())

    current_date = date.today()

    current_leakage_info = 50

    current_consumption_info = {
        "outlet_1": 250,
        "outlet_2": 200
    }
    current_consumption = 600
    outlets = list(current_consumption_info.keys())
    outlets_data = list(current_consumption_info.values())

    # hourly_consumption = []
    hourly_consumption_dict = {
        "0": "2",
        "1": "3",
        "2": "4",
        "3": "5",
        "4": "4",
        "5": "5",
        "6": "4",

    }
    # for i in hourly_consumption:
    #     time = int(i['time'])
    #     parsed_time = datetime.fromtimestamp(time).hour
    #     total_volume = int(i['outlet1_volume']) + int(i['outlet2_volume'])

    #     hourly_consumption_dict[parsed_time] = total_volume

    hours = list(hourly_consumption_dict.keys())
    hour_consumption = list(hourly_consumption_dict.values())
    hour_consumption2 = [20,30]

    return render_template('dashboard/dashboard.html',
                           apartment_names=apartment_names,
                           weeks=weeks,
                           current_date=current_date,
                           current_leakage_info=current_leakage_info,
                           current_consumption=current_consumption,
                           current_consumption_info=current_consumption_info,
                           outlets=outlets,
                           outlets_data=outlets_data,
                           hours=hours,
                           hour_consumption=hour_consumption,
                           apartment1=apartment1,
                           apartment2=apartment2,
                           apartment3=apartment3,
                           apartment4=apartment4,
                           apartment5=apartment5,
                           )
