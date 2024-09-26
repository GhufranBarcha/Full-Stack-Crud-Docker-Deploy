from config import db, app

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
        }

# Ensure the tables are created using the same db instance, inside the application context
def create_tables():
    with app.app_context():  # Add this line to provide the application context
        db.create_all()

# Now you can call create_tables() after defining the models
create_tables()
