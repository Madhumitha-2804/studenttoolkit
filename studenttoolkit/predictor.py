def predict(current_cgpa, semesters, future_gpa):
    return round(
        ((current_cgpa * semesters) + future_gpa)
        / (semesters + 1),
        2
    )