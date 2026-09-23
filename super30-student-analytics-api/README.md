# Super30 Student Analytics API

A student analytics system combining a FastAPI GET API, NumPy calculations, and Plotly visualizations.

## Project structure

- `students.csv`: dataset containing 20 students and marks in three subjects
- `analytics.py`: shared CSV loading and NumPy analysis functions
- `app.py`: FastAPI GET API
- `visualization.py`: Plotly chart generator
- `output/`: generated interactive HTML charts

## Installation

From this project directory:

```bash
pip install -r requirements.txt
```

## Run the FastAPI server

```bash
uvicorn app:app --reload
```

The API is available at http://127.0.0.1:8000.

Interactive API documentation is available at:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## GET endpoints

| Endpoint | Purpose |
| --- | --- |
| `GET /students` | Return all students |
| `GET /student/5` | Return student ID 5 |
| `GET /average/python` | NumPy average for Python |
| `GET /average/mathematics` | NumPy average for Mathematics |
| `GET /average/data-science` | NumPy average for Data Science |
| `GET /topper` | Return the highest overall-average student |
| `GET /passed` | Students with at least 40 in every subject |
| `GET /failed` | Students below 40 in at least one subject |
| `GET /statistics` | Subject averages, highest, lowest, and overall average |

Example requests:

```text
http://127.0.0.1:8000/students
http://127.0.0.1:8000/student/5
http://127.0.0.1:8000/average/python
http://127.0.0.1:8000/topper
http://127.0.0.1:8000/statistics
```

## Create Plotly visualizations

```bash
python visualization.py
```

This creates:

- `output/average_marks.html`: bar chart comparing average marks across subjects
- `output/top_five_students.html`: bar chart comparing the top five students

Open either HTML file in a browser to interact with the chart.

## Analysis observations

1. Mathematics has the highest average mark among the three subjects.
2. Data Science is close behind Mathematics, showing generally strong performance.
3. Kiara Nair is the topper because her overall average is the highest in the dataset.
4. Ananya Singh and Meera Iyer are also among the strongest all-round performers.
5. Most students pass every subject under the minimum mark of 40 criterion.
6. Student 11 is the only failed student because the Python mark is below 40.
7. The lowest marks occur in Python, so Python has the widest opportunity for improvement.

## Demonstration flow

For the video demonstration, show the CSV data, explain the NumPy calculations in `analytics.py`, start the FastAPI server, execute at least six GET endpoints in Swagger UI, run `visualization.py`, and open both Plotly HTML charts.

## Submission

- GitHub repository: `super30-student-analytics-api`
- Author/student: Sudhanshu
- YouTube demonstration: add the published video link here
