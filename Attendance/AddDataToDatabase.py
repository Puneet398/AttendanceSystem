import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://attendance-44d4c-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "Puneet":
        {
            "name": "Puneet Pahuja",
            "Branch": "Computer Science",
            "StartingYear": 2021,
            "TotalAttendance": 20,
            "Sem.": 5,
            "LastAttendanceTime": "2023-11-24 00:30:00"
        },
    "vishwash":
        {
            "name": "Vishwash Raushan",
            "Branch": "Computer Science",
            "StartingYear": 2021,
            "TotalAttendance": 21,
            "Sem.": 5,
            "LastAttendanceTime": "2023-11-24 00:30:00"
        },
    "sanjay":
        {
            "name": "J Sanjay Chandra",
            "Branch": "Computer Science",
            "StartingYear": 2021,
            "TotalAttendance": 19,
            "Sem.": 5,
            "LastAttendanceTime": "2023-11-24 00:30:00"
        }
}

for key, value in data.items():
    ref.child(key).set(value)