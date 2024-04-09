import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-4b999-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "11111":
        {
            "name": "Elon Musk",
            "Major": "BSC",
            "starting_year":1992,
            "Total Attendance":6,
            "Standing": "G",
            "Year":"4",
            "Last_attendance_time": "2022-12-11 00:54:34"
        },
    "22222":
        {
            "name": "Siddharth R",
            "Major": "CSE",
            "starting_year": 2022,
            "Total Attendance": 10,
            "Standing": "G",
            "Year": "4",
            "Last_attendance_time": "2024-04-08 09:45:34"
        },
    "33333":
        {
            "name": "Tom George",
            "Major": "CSE",
            "starting_year": 2022,
            "Total Attendance": 9,
            "Standing": "G",
            "Year": "4",
            "Last_attendance_time": "2024-04-04 16:00:12"
        }
}

for key,value in data.items():
    ref.child(key).set(value)