import pandas as pd
import random
from datetime import datetime, timedelta

departments = ["CSE", "IT", "ECE", "ME"]
complaint_types = ["Electrical", "Water", "Cleanliness"]
guards = ["Guard Raj", "Guard Mohan", "Guard Suresh"]
locations = ["Block A", "Block B", "Block C", "Hostel 1", "Hostel 2", "Seminar Hall", "Computer Lab"]

data = []

for i in range(1, 101):
    status = random.choice(["Pending", "In Progress", "Completed"])
    guard = random.choice(guards) if status != "Pending" else ""
    
    created = datetime(2026, 2, 1) + timedelta(days=random.randint(0, 10))
    updated = created + timedelta(hours=random.randint(1, 48)) if status != "Pending" else ""

    data.append([
        f"C{i:03}",
        f"S{100+i}",
        f"Student_{i}",
        random.choice(departments),
        random.choice(complaint_types),
        "Sample complaint description",
        random.choice(locations),
        status,
        guard,
        created,
        updated
    ])

df = pd.DataFrame(data, columns=[
    "complaint_id","student_id","student_name","department",
    "complaint_type","description","location",
    "status","assigned_guard","created_at","updated_at"
])

df.to_csv("complaints.csv", index=False)

print("100 complaint records generated successfully!")
