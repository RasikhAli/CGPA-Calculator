from flask import Flask, render_template, request, jsonify
from calculations import calculate_gpa

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    print(data)
    subjects = {key: value for key, value in data.items() if key.startswith('subject')}
    marks = {key: value for key, value in data.items() if key.startswith('marks')}
    credit_hours = {key: value for key, value in data.items() if key.startswith('credits')}
    
    previous_cgpa = float(data.get('previous_cgpa', 0.0)) if data.get('previous_cgpa') else 0.0
    previous_credits = int(data.get('previous_credits', 0)) if data.get('previous_credits') else 0
    is_first_semester = data.get('firstSemesterLabel') == 'on'
    
    sgpa, cgpa, grades = calculate_gpa(subjects, marks, credit_hours, is_first_semester, previous_cgpa, previous_credits)
    
    return jsonify({
        'sgpa': sgpa,
        'cgpa': cgpa,
        'grades': grades,
        'subjects': subjects,
        'marks': marks,
        'credit_hours': credit_hours
    })

if __name__ == '__main__':
    app.run(debug=True)
