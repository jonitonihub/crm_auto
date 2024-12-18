from ..extensions import db, loginManager
from datetime import datetime
from flask_login import UserMixin
from .user import User

  
    
class Car(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    car_brand_id = db.Column(db.Integer, nullable=False)  # carBrandId
    car_model_id = db.Column(db.Integer, nullable=False)  # carModelId
    initial_mileage = db.Column(db.Integer, nullable=False)  # initialMileage
    updated_mileage_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # updatedMileageAt
    car_created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # carCreatedAt
    mileage = db.Column(db.Integer, nullable=False)  # mileage
    brand = db.Column(db.String(50), nullable=False)  # brand
    model = db.Column(db.String(50), nullable=False)  # model
    logo = db.Column(db.String(200), nullable=True)  # logo
    
