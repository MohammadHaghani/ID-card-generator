import random
from datetime import datetime

last_year = datetime.now().year % 100
unique_number = f"{random.randrange(99999):05d}"
control_number = str(last_year) + str(unique_number)
total = 0
for i in control_number:
    total += int(i)
control_number = total % 10
id_generator = f"{last_year}{unique_number}{control_number}"
    
print(f"Generated Student ID: {id_generator}")
