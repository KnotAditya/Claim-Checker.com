from flask import Flask, render_template, request
import database
app = Flask(__name__)

vidur_account = database.vidur_account

@app.route('/')
@app.route('/submit-id-info', methods=['GET', 'POST'])

def process_id_info():
    if request.method == 'POST':
        id_number = str(request.form['idNumber'])
        full_name = str(request.form['fullName'])
        date_of_birth = str(request.form['dob'])
        nationality = str(request.form['nationality'])

        # Check if the ID number is exactly 14 digits
        if len(id_number) != 14 or not id_number.isdigit():
            message = "Invalid ID number"
            return render_template('index.html', message=message)
        
        print(vidur_account)
        
        Number = False
        Name = False
        dob = False
        Nation = False
        
        print(id_number)
        if id_number == vidur_account["emirates_IDs"]:
            Number = True
        
        if full_name == vidur_account["Full_name"]:
            Name = True

        if date_of_birth == vidur_account["dateofbirth"]:
            dob = True

        if nationality == vidur_account["Nationality"]:
            Nation = True
        
        print(Number)
        print(Name)
        print(dob)
        print(Nation)
                
        if Number and Name and dob and Nation:
            response = f"Hello {full_name}, your information has been recorded"
            return response
        
        else:
            message = "Invalid information. Please enter the correct information"
            return render_template('index.html', message=message)

    return render_template('index.html', message='')

if __name__ == '__main__':
    app.run(debug=True)

