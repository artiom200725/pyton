def vibration_diagnostic(vibe_data):
    if not vibe_data:
        return 0.0  
    alarm_count = 0
    for v in vibe_data:
        if v >= 7.1:
            alarm_count += 1       
    return (alarm_count / len(vibe_data)) * 100
vibe_data = [1.5, 2.7, 3.0, 5.5, 7.2, 8.0, 2.0]
print(vibration_diagnostic(vibe_data))

