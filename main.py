from fastapi import FastAPI
import json
app = FastAPI()
def load_data():
    with open('students_data.json','r') as f:
        data = json.load(f)
        return data
@app.get("/")
def hello():
    return {"message": "Hello, World!"} 

@app.get("/view")
def view():
    data = load_data()
    return data
@app.get("/view/{student_id}")
def view_student(student_id: str):
    data = load_data()
    students = data['students']
    j = 0
    for student in students:
        if student['bt_id'] == student_id:
            j = 1
            return student
    if j==0:
        return {'error': 'Student not found'}
       
    