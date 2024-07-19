def calculate_gpa(subjects, marks, credit_hours, is_first_semester, previous_cgpa=0, previous_credits=0):
    total_credits = sum([int(credit_hours[key]) for key in credit_hours])
    total_points = 0
    
    grades = {}
    
    for key in marks:
        subject_key = key.split('_')[-1]
        mark = int(marks[key])
        credit = int(credit_hours[f'credits_{subject_key}'])
        
        if mark > 84:
            grade_point = 4.0
        elif mark > 79:
            grade_point = 3.66
        elif mark > 74:
            grade_point = 3.33
        elif mark > 70:
            grade_point = 3.0
        elif mark > 67:
            grade_point = 2.66
        elif mark > 63:
            grade_point = 2.33
        elif mark > 60:
            grade_point = 2.0
        elif mark > 57:
            grade_point = 1.66
        elif mark > 53:
            grade_point = 1.33
        elif mark > 49:
            grade_point = 1.0
        else:
            grade_point = 0.0
        
        total_points += grade_point * credit
        grades[subject_key] = grade_point_to_grade(grade_point)
    
    sgpa = total_points / total_credits
    
    if not is_first_semester:
        cgpa = ((previous_cgpa * previous_credits) + (sgpa * total_credits)) / (previous_credits + total_credits)
    else:
        cgpa = sgpa
    
    return round(sgpa, 2), round(cgpa, 2), grades

def grade_point_to_grade(grade_point):
    if grade_point == 4:
        return 'A'
    elif grade_point >= 3.66:
        return 'A-'
    elif grade_point >= 3.33:
        return 'B+'
    elif grade_point >= 3:
        return 'B'
    elif grade_point >= 2.66:
        return 'B-'
    elif grade_point >= 2.33:
        return 'C+'
    elif grade_point >= 2:
        return 'C'
    elif grade_point >= 1.66:
        return 'C-'
    elif grade_point >= 1.33:
        return 'D+'
    elif grade_point >= 1:
        return 'D'
    else:
        return 'F'
