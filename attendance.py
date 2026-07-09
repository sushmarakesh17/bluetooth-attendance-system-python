import pandas as pd
from datetime import datetime
import os

ATTENDANCE_FILE = "attendance.csv"

def mark_attendance(student):

    now = datetime.now()

    record = {
        "Name": student["Name"],
        "USN": student["USN"],
        "Bluetooth MAC": student["Bluetooth MAC"],
        "Date": now.strftime("%Y-%m-%d"),
        "Time": now.strftime("%H:%M:%S")
    }

    if os.path.exists(ATTENDANCE_FILE):
        df = pd.read_csv(ATTENDANCE_FILE)
    else:
        df = pd.DataFrame(columns=record.keys())

    duplicate = (
        (df["USN"] == student["USN"]) &
        (df["Date"] == record["Date"])
    )

    if duplicate.any():
        return False

    df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)

    df.to_csv(ATTENDANCE_FILE, index=False)

    return True