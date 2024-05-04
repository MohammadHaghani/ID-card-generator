import random
from datetime import datetime

year_last_digits = datetime.now().year % 100
unique_number = f"{random.randrange(99999):05d}"
control_digit = str(year_last_digits) + str(unique_number)
total = 0
for i in control_digit:
    total += int(i)
control_digit = total % 10
student_id = f"{year_last_digits}{unique_number}{control_digit}"
    
print(f"Generated Student ID: {student_id}")
