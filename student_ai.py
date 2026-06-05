print("===================================")
print("   STUDENT AI SCORE PREDICTOR")
print("===================================")

study_hours = float(input("Enter Study Hours: "))
attendance = float(input("Enter Attendance %: "))
assignments = float(input("Enter Assignment %: "))

score = (study_hours * 4) + (attendance * 0.5) + (assignments * 0.5)

print("\n-----------------------------------")
print("Predicted Score:", score)

if score >= 90:
    print("Grade: A+")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: D")

print("-----------------------------------")