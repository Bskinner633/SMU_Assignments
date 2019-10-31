from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect database and tables
Base = automap_base()
base.prepare(engine, reflect = True)

# save table references
Measurement = Base.classes.measurement
Station = Base.classes.station 

# create session 
session = Sesssion(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

endDate = (session.query(Measurment.date).order_by(Measurement.date.desc()).first())

lastYear = dt.date(2017, 8, 23) - dt.timedelta(days=365)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    return (
        f"Welcome to the Weater API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/precipitation/<start_date/<end_date>"
        f"/api/v1.0/tobs/<start_date>/<end_date>"
        f"/api/v1.0/tobs/<tripStart>/<tripEnd>"
    )

@app.route("/api/v1.0/precipitation/")
def get_precipitation():
    conn = engine.connect()

    precipQuery = f"""
                SELECT
                    date,
                    prcp
                FROM
                    measurement
                """

    df = pd.read_sql(precipQuery, conn)
    return jsonify(df.to_json())

@app.route("/api/v1.0/precipitation/<start_date>/<end_date>")
def get_precipitation_forDates(start_date, end_date):
    conn = engine.connect()

    precipQuery = f"""
                SELECT
                    date,
                    prcp
                FROM
                    measurement
                WHERE
                    date > '{start_date}'
                    AND date <= '{end_date}'
                """

    df = pd.read_sql(precipQuery, conn)
    return jsonify(df.to_json())

@app.route("/api/v1.0/tobs/<start_date>/<end_date>")
def get_temperature_forDates(start_date, end_date):
    conn = engine.connect()

    tempQuery = f"""
                SELECT
                    tobs                    
                FROM
                    measurement
                WHERE
                    date > '{start_date}'
                    AND date <= '{end_date}'
                """

    df = pd.read_sql(tempQuery, conn)
    return jsonify(df.to_json())


@app.route("/api/v1.0/stations/")
def get_stations():
    conn = engine.connect()

    stationQuery = f"""
                SELECT
                    stations,
                    name
                FROM
                    station
                """

    df = pd.read_sql(stationQuery, conn)
    return jsonify(df.to_json())

@app.route("/api/v1.0/tobs/<tripStart>/<tripEnd>")
def get_temperature_forDates(tripStart, tripEnd):
    conn = engine.connect()

    tripTempQuery = f"""
                SELECT
                    MAX(tobs),
                    MIN(tobs),
                    ROUND(AVG(tobs),2)tobs                    
                FROM
                    measurement
                WHERE
                    date > '{tripStart}'
                    AND date <= '{tripEnd}'
                """

    df = pd.read_sql(tripTempQuery, conn)
    return jsonify(df.to_json())

if __name__ == "__main__":
    app.run(debug=True)
