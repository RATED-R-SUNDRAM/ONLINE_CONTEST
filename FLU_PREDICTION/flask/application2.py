#%%
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

#%%
app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'
db = SQLAlchemy(app)
class drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.String(80), nullable=False)

@app.route('/') 
def hello_world(): 
    return 'Hello, World!'
@app.route('/predict')
def predict(): 
    return "prediction"



# %%
