from flask import Flask, render_template, request

app = Flask(__name__)

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

        response = f"Received Emirates ID information:\n - Full Name: {full_name}\n - ID Number: {id_number}\n - Date of Birth: {date_of_birth}\n - Nationality: {nationality}"
        return response

    return render_template('index.html', message='')

if __name__ == '__main__':
    app.run(debug=True)

