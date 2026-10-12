"""
AGRICONNECT - Database Models
User Module:        User table
Marketplace Module:  Listing table, ContactRequest table
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), nullable=False)   # 'farmer' or 'buyer'

    # --- login attempt limiting ---
    failed_attempts = db.Column(db.Integer, default=0, nullable=False)
    locked_until = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<User {self.name} ({self.role})>"


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    farmer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    crop_name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20), nullable=False, default='kg')   # kg or quintal
    price_per_unit = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(300), nullable=True)

    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True, nullable=False)   # False = marked as sold

    farmer = db.relationship('User', backref='listings')

    def __repr__(self):
        return f"<Listing {self.crop_name} by {self.farmer_id}>"


class ContactRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'), nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    message = db.Column(db.String(300), nullable=True)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)

    listing = db.relationship('Listing', backref='contact_requests')
    buyer = db.relationship('User', backref='sent_requests')

    def __repr__(self):
        return f"<ContactRequest listing={self.listing_id} buyer={self.buyer_id}>"


class AdvisoryRule(db.Model):
    """
    A single row of the rule-based Crop Advisory engine.
    crop + symptom (+ optional soil) -> issue + recommendation.

    soil = 'Any' means this rule applies regardless of soil condition.
    A more specific (crop, soil, symptom) match is preferred over a
    (crop, 'Any', symptom) match when both exist — see get_advisory() in app.py.
    """
    id = db.Column(db.Integer, primary_key=True)
    crop = db.Column(db.String(50), nullable=False)
    soil = db.Column(db.String(30), nullable=False, default='Any')   # Normal / Waterlogged / Dry / Any
    symptom = db.Column(db.String(80), nullable=False)
    issue = db.Column(db.String(120), nullable=False)
    recommendation = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f"<AdvisoryRule {self.crop}/{self.soil}/{self.symptom} -> {self.issue}>"
