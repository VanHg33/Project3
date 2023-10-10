from flask import Flask, jsonify, render_template
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime as dt
import pandas as pd
import numpy as np
import sqlite3


engine = create_engine("sqlite:///JSearchdata.sqlite")
Base = declarative_base()

class json_data(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    employer_name = Column(String(255), nullable=False)
    job_publisher = Column(String(255), nullable=False)
    job_employment_type = Column(String(100))
    job_title = Column(String)
    job_apply_link = Column(String)
    job_description = Column(String)
    job_city = Column(String)
    job_state =Column(String)
    job_latitude =Column(String)
    job_longitude = Column(String)
    job_required_education_bachelors_degree =Column(String)


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

# Query the data from the "jobs" table
jobs_data = session.query(json_data.id, json_data.employer_name).all()

# Close the session
session.close()

#Create an app
app = Flask(__name__)



# Define a route to retrieve data with state and job employment type information
@app.route("/employment")
def get_data():
    try:
        # # Connect to the SQLite database
        conn = sqlite3.connect('JSearchdata.sqlite')  # Updated with the correct database file name
        cursor = conn.cursor()

        # Execute a query to retrieve data with state and job employment type information
        cursor.execute("SELECT job_state, job_employment_type, COUNT(*) FROM json_data GROUP BY job_state, job_employment_type")

        # Fetch all the data
        data = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Prepare data for sending as JSON
        result = [{'state': row[0], 'employment_type': row[1], 'count': row[2]} for row in data]

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})



# Define the first API route to get all rows from the "jobs" table
# @app.route('/api/v1.0/jobs')
# def get_jobs():
#     # Create a database engine
#     engine = create_engine()

#     # Query the "jobs" table and load the results into a Pandas DataFrame
#     df = pd.read_sql_table('jobs', engine)

#     # Convert the DataFrame to a JSON object and return it
#     return jsonify(df.to_dict(orient='records'))


# @app.route("/api/v1.0/employment")
# def stations():
#     companies = session.query(data.employment_name).all()
#     result_comp = list(np.ravel(companies))
#     session.close()
#     return jsonify(result_comp)

# @app.route("/api/v1.0/education")


#Define index route
@app.route("/")
def index():
    return render_template('index.html')

# Define the route to render the dashboard page:
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/employment")
def employment():
    return render_template("employment.html")


# @app.route("/api/v1.0/companies")
# def stations():
#     companies = session.query(data.employment_name).all()
#     result_comp = list(np.ravel(companies))
#     session.close()
#     return jsonify(result_comp)






if __name__ == '__main__':
    app.run(debug=True)

