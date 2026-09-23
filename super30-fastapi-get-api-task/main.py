"""Fast GET API Fundamentals using FastAPI."""

from fastapi import FastAPI


app = FastAPI(
    title="Fast GET API Fundamentals",
    description="Beginner-friendly GET endpoints using static and dynamic paths.",
    version="1.0.0",
)



@app.get("/")
def home():
    return {"message": "Welcome to Super30 FastAPI"}


@app.get("/student")
def student():
    return {"name": "Sudhanshu", "batch": "Super30", "role": "Student"}


@app.get("/course")
def course():
    return {
        "course_name": "Backend Development with FastAPI",
        "mentor": "Sudhanshu",
        "duration": "8 Weeks",
        "topics": ["Python", "FastAPI", "REST API", "Database", "Deployment"],
    }


@app.get("/skills")
def skills():
    return {"skills": ["Python", "FastAPI", "SQL", "Docker", "AWS"]}


@app.get("/add/{num1}/{num2}")
def add(num1: int, num2: int):
    return {"result": num1 + num2}


@app.get("/multiply/{num1}/{num2}")
def multiply(num1: int, num2: int):
    return {"result": num1 * num2}


@app.get("/square/{number}")
def square(number: int):
    return {"number": number, "square": number**2}


@app.get("/check/{number}")
def check_even_or_odd(number: int):
    return {"number": number, "type": "even" if number % 2 == 0 else "odd"}


@app.get("/age/{age}")
def age_message(age: int):
    if age < 0:
        message = "Age cannot be negative."
    elif age < 13:
        message = "You are a child."
    elif age < 20:
        message = "You are a teenager."
    elif age < 60:
        message = "You are an adult."
    else:
        message = "You are a senior citizen."
    return {"age": age, "message": message}


@app.get("/table/{number}")
def multiplication_table(number: int):
    return {
        "number": number,
        "table": [
            f"{number} x {multiplier} = {number * multiplier}"
            for multiplier in range(1, 11)
        ],
    }


@app.get("/profile/{name}/{age}")
def profile(name: str, age: int):
    return {"name": name, "age": age}


@app.get("/number/{number}")
def number_analysis(number: int):
    return {
        "number": number,
        "square": number**2,
        "cube": number**3,
        "even": number % 2 == 0,
    }
