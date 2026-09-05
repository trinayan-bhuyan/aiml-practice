# Lesson 8: Repetition with while loops

pressure = 10.0

# The loop runs as long as the condition remains True
while pressure < 50.0:
    print(f"Pumping in progress... Current pressure: {pressure:.1f} bar")
    pressure += 10.0  # Equivalent to: pressure = pressure + 10.0

print(f"Target pressure reached: {pressure:.1f} bar. Pump deactivated.")