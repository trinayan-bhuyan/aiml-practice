# Lesson 7: Logical Operators (and, or, not)

temp = float(input("Enter temperature (°C): "))
pressure = float(input("Enter pressure (bar): "))

# 'and' requires both conditions to evaluate to True
if temp <= 100 and pressure <= 150:
    print("STATUS NORMAL: System operating safely.")
else:
    print("ALERT: One or more parameters exceed safe thresholds!")