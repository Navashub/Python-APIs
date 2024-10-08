# from flask import Flask
# app = Flask(__name__)
# from flask_sqlalchemy import SQLAlchemy 


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# db = SQLAlchemy(app)

# class Drink(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     description = db.Column(db.String(120))

#     def __repr__(self):
#         return f"{self.name} - {self.description}"

# @app.route('/')
# def index():
#     return 'Hello'

# @app.route('/drinks')
# def get_drinks():
#     return {"drinks": "drink data"}


# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()


from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Correct the SQLite URI to use a relative path or absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # For a relative path to the current directory
# or 'sqlite:////full/path/to/data.db' for an absolute path

db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return 'Hello'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}

        output.append(drink_data)

    return {"drinks": output}


@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}


@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'], description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

if __name__ == '__main__':
    # Ensure the app context is used when creating the database
    with app.app_context():
        db.create_all()
    app.run(debug=True)
