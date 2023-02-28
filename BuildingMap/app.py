from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///buildings.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/add_building', methods=['POST'])
def add_building():
    name = request.form['name']
    address = request.form['address']
    latitude = float(request.form['latitude'])
    longitude = float(request.form['longitude'])
    building = Building(name=name, address=address, latitude=latitude, longitude=longitude)
    db.session.add(building)
    db.session.commit()
    return jsonify({'result': 'success'})

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(100))
address = db.Column(db.String(200))
latitude = db.Column(db.Float)
longitude = db.Column(db.Float)
   

    
if __name__ == "__main__":
    app.run(debug=True)

  