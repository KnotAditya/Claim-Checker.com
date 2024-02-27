from flask import Flask, render_template, request
import database
app = Flask(__name__)

vidur_account = database.vidur_account

@app.route('/')
@app.route('/submit-id-info', methods=['GET', 'POST'])

def process_id_info():
    if request.method == 'POST':
        id_number = request.form['idNumber']
        full_name = request.form['fullName']
        date_of_birth = request.form['dob']
        nationality = request.form['nationality']

        # Check if the ID number is exactly 14 digits
        if len(id_number) != 14 or not id_number.isdigit():
            message = "Invalid ID number"
            return render_template('index.html', message=message)
        
        account = [id_number, full_name, date_of_birth, nationality]
        id_number == False
        full_name == False
        date_of_birth == False
        nationality == False
        
        if id_number == database.emriates_IDs:
            id_number == True
        
        if full_name == database.Full_name:
            full_name == True

        if date_of_birth == database.dateofbirth:
            date_of_birth == True

        if nationality == database.Nationality:
            nationality == True
        
        if account == True:
            response = f"Hello {full_name}, your information has been recorded"
            return response
        
        if account != True:
            message = "Invalid information. Please enter the correct information"
            return render_template('index.html', message=message)

    return render_template('index.html', message='')

if __name__ == '__main__':
    app.run(debug=True)

