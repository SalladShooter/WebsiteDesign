from flask import Flask, render_template, request
import json
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        if request.method == 'POST':
            # Get form data
            reservation_name = request.form['reservation_name']
            reservation_date = request.form['reservation_date']
            reservation_details = request.form['reservation_details']

            reservation = {
                'name': reservation_name,
                'date': reservation_date,
                'details': reservation_details
            }
            save_reservation_to_json(reservation)

            return render_template('success.html', message="Form submitted successfully")
    except Exception as e:
        traceback.print_exc()
        return render_template('error.html', message=f"An error occurred: {e}")

def save_reservation_to_json(reservation):
    with open('database/reservation.json', 'a') as json_file:
        json.dump(reservation, json_file)
        json_file.write('\n\n')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
