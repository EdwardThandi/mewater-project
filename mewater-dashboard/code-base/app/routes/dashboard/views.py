from flask import Blueprint, render_template
from datetime import datetime, date
from app import db
from app.models import ApartmentWaterConsumption, IotWaterConsumption
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

    # latest_outlet_data = db.session.query(IotWaterConsumption).first()
    latest_outlet_data = db.session.query(IotWaterConsumption).order_by(IotWaterConsumption.id.desc()).limit(6).all()

    print(latest_outlet_data)


    current_consumption_data = latest_outlet_data[0]
    current_consumption_info = {
        "outlet_1": current_consumption_data.meter2Volume,
        "outlet_2": current_consumption_data.meter3Volume,
    }
    current_consumption = float(
        current_consumption_data.meter2Volume) + float(current_consumption_data.meter3Volume)
    outlets = list(current_consumption_info.keys())
    outlets_data = list(current_consumption_info.values())
    
    current_leakage_info = float(current_consumption_data.meter1Volume) - current_consumption

    hourly_consumption_dict = {}
    for i, data in enumerate(latest_outlet_data):

        total_volume = float(data.meter2Volume) + float(data.meter3Volume)

        hourly_consumption_dict[i] = total_volume

    hours = list(hourly_consumption_dict.keys())
    hour_consumption = list(hourly_consumption_dict.values())

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
