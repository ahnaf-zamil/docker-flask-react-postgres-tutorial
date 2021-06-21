from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_cors import CORS, cross_origin

import os
import time

time.sleep(5)

app = Flask(__name__)
cors = CORS(app)
app.config["SECRET_KEY"] = "pogchampsecret"
app.config["CORS_HEADERS"] = "Content-Type"
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://postgres:{os.environ['POSTGRES_PASSWORD']}@postgres:5432/{os.environ['POSTGRES_DB']}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
db = SQLAlchemy(app)


class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())


db.create_all()

admin = Admin(app, name="Programming Languages", template_mode="bootstrap3")
admin.add_view(ModelView(Language, db.session))


@app.route("/")
def home():
    return jsonify(
        {
            "status": "online",
        }
    )


@app.route("/languages")
@cross_origin()
def get_languages():

    languages = Language.query.all()

    return jsonify({"data": [{"name": lang.name} for lang in languages]})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
