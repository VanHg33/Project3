from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Define the route to your HTML page
@app.route('/')
def index():
    return render_template('employment.html')

# Define a route to retrieve data with state and job employment type information
@app.route('/data')
def get_data():
    try:
        # Connect to the SQLite database
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

if __name__ == '__main__':
    app.run(debug=True)

