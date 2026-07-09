import streamlit as st
from bluetooth_scanner import scan_devices
from database import load_students
from attendance import mark_attendance

st.title("Bluetooth Based Attendance System")

if st.button("Scan Bluetooth Devices"):

    devices = scan_devices()
    students = load_students()

    count = 0

    for device in devices:

        match = students[
            students["Bluetooth MAC"] == device["mac"]
        ]

        if not match.empty:

            student = match.iloc[0]

            if mark_attendance(student):
                st.success(f"{student['Name']} Attendance Marked")
                count += 1

    if count == 0:
        st.warning("No Registered Students Found")