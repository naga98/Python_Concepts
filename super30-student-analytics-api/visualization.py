"""Create Plotly visualizations for the student dataset."""

from pathlib import Path

import plotly.graph_objects as go

from analytics import SUBJECTS, load_students, marks_array, overall_averages, subject_averages


OUTPUT_DIR = Path(__file__).with_name("output")


def create_visualizations():
    students = load_students()
    OUTPUT_DIR.mkdir(exist_ok=True)

    averages = subject_averages(students)
    average_chart = go.Figure(
        data=[go.Bar(x=list(averages.keys()), y=list(averages.values()), marker_color="#2563eb")]
    )
    average_chart.update_layout(
        title="Average Marks by Subject",
        xaxis_title="Subject",
        yaxis_title="Average Marks",
        yaxis_range=[0, 100],
    )
    average_chart.write_html(OUTPUT_DIR / "average_marks.html")

    scores = overall_averages(students)
    top_indices = scores.argsort()[-5:][::-1]
    top_names = [students[index]["name"] for index in top_indices]
    top_scores = [round(float(scores[index]), 2) for index in top_indices]
    top_chart = go.Figure(
        data=[go.Bar(x=top_names, y=top_scores, marker_color="#16a34a")]
    )
    top_chart.update_layout(
        title="Top Five Students by Overall Average",
        xaxis_title="Student",
        yaxis_title="Overall Average",
        yaxis_range=[0, 100],
    )
    top_chart.write_html(OUTPUT_DIR / "top_five_students.html")


if __name__ == "__main__":
    create_visualizations()
    print("Created output/average_marks.html")
    print("Created output/top_five_students.html")
