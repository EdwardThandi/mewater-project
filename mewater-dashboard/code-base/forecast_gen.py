from app.models import WaterForecast
from app import db, create_app
from datetime import datetime


with create_app().app_context():
    user_id = 1
    projected_weekly_water = 'CLOSED'
    date = str(datetime.today().date())

    forecast = WaterForecast(
        user_id=user_id,
        projected_weekly_water=projected_weekly_water,
        date=date
    )

    db.session.add(forecast)
    db.session.commit()

    print(f'Forecast Added: {projected_weekly_water}')
