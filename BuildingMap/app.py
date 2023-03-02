from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
# PostgreSQL database connection details
host = "postgresql-dev-kartai.postgres.database.azure.com"
port = "5432"
database = "kartai_bachelor_2023"
user = "kartai_bachelor_2023@postgresql-dev-kartai"
password = "Io4$7M1e"



# Configure app to use PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{user}:{password}@{host}:{port}/{database}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/save-building', methods=['POST'])
def save_building():
    name = request.form['name']
    address = request.form['address']
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    # Insert data into the database
    try:
        building = Building(name=name, address=address, latitude=latitude, longitude=longitude)
        db.session.add(building)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Building saved successfully'})
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'message': 'Failed to save building'})


if __name__ == "__main__":
    app.run(debug=True)
