import pandas as pd

STUDENT_FILE = "students.csv"

def load_students():
    return pd.read_csv(STUDENT_FILE)