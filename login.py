from flask import Flask, render_template, request
import database

app = Flask(__name__, static_folder='static')

vidur_account = database.vidur_account

@app.route('/')
@app.route('/submit-id-info', methods=['GET', 'POST'])

def process_id_info():
    if request.method == 'POST':
        id_number = request.form['idNumber']
        full_name = request.form['fullName']
        date_of_birth = request.form['dob']
        nationality = request.form['nationality']

        # Validate the provided information
        if (len(id_number) == 14 and id_number.isdigit() and
            id_number == vidur_account["emirates_IDs"] and 
            full_name == vidur_account["Full_name"] and 
            date_of_birth == vidur_account["dateofbirth"] and 
            nationality == vidur_account["Nationality"]):
            # Redirect to success page if validation is successful
            return render_template('result.html', full_name=full_name)
        else:
            # Stay on the current page and show an error message if validation fails
            message = "Invalid information. Please enter the correct information."
            return render_template('index.html', message=message)

    # Initial page load or GET request
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)