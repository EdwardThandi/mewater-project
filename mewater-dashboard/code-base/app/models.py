from app import db


class ApartmentWaterConsumption(db.Model):
    __tablename__ = 'apartment_water_consumption'

    id = db.Column(db.Integer, primary_key=True)
    apartment_name = db.Column(db.String(50), nullable=False)
    instance_1 = db.Column(db.String(50), nullable=False)
    instance_2 = db.Column(db.String(50), nullable=False)
    instance_3 = db.Column(db.String(50), nullable=False)
    instance_4 = db.Column(db.String(50), nullable=False)
    instance_5 = db.Column(db.String(50), nullable=False)
    instance_6 = db.Column(db.String(50), nullable=False)


class IotWaterConsumption(db.Model):
    __tablename__ = 'iot_water_consumption'

    id = db.Column(db.Integer, primary_key=True)
    meter1Flowrate = db.Column(db.Float, nullable=True)
    meter2Flowrate = db.Column(db.Float, nullable=True)
    meter3Flowrate = db.Column(db.Float, nullable=True)
    meter1Volume = db.Column(db.Float, nullable=True)
    meter2Volume = db.Column(db.Float, nullable=True)
    meter3Volume = db.Column(db.Float, nullable=True)
