# Lesson 6: Multi-branch Decision Making (if / elif / else)

pressure = float(input("Enter pipeline pressure (bar): "))

if pressure > 150:
    print("CRITICAL: Overpressure detected! Vent valve opening.")
elif pressure < 50:
    print("WARNING: Low pressure detected. Check feed pump.")
else: 
    print("STATUS NORMAL: Operation pressure within safe parameters.")