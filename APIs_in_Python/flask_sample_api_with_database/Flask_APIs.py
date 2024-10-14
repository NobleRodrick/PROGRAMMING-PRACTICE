from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True) # type: ignore
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.name} - {self.description}"
   

 
@app.route('/')
def index():
    return 'Hello World!'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    
    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    
    return {'drinks': output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return ({'name': drink.name, 'description': drink.description})

@app.route('/drinks', methods=['POST'])
def add_drink():
    data = request.json
    # Check if the drink name already exists
    existing_drink = Drink.query.filter_by(name=data['name']).first()

    if existing_drink:
        return {'error': 'A drink with this name already exists!'}, 400

    # Create a new drink if it doesn't exist
    new_drink = Drink(name=data['name'], description=data['description'])
    db.session.add(new_drink)
    db.session.commit()

    return {'id': new_drink.id}, 201


@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get_or_404(id)
    db.session.delete(drink)
    db.session.commit()
    return {'deleted': True}

if __name__ == '__main__':
    app.run(debug=True)