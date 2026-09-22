from pathlib import Path

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_figure(figure, filename):
    """Write an interactive Plotly figure to the output directory."""
    path = OUTPUT_DIR / filename
    figure.write_html(path, include_plotlyjs="cdn")
    print(f"Created: {path}")


# 1. Bar chart: monthly sales
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 170, 140, 200, 230]
bar = go.Figure(go.Bar(x=months, y=sales, name="Sales", marker_color="#2563eb"))
bar.update_layout(title="Monthly Sales - Bar Chart", xaxis_title="Month", yaxis_title="Sales (units)")
save_figure(bar, "01_monthly_sales_bar.html")

# 2. Line chart: the same monthly sales
line = go.Figure(go.Scatter(x=months, y=sales, mode="lines+markers", name="Sales", line_color="#dc2626"))
line.update_layout(title="Monthly Sales Trend - Line Chart", xaxis_title="Month", yaxis_title="Sales (units)")
save_figure(line, "02_monthly_sales_line.html")

# 3. Pie chart: department distribution
departments = ["Engineering", "Sales", "Marketing", "HR", "Operations"]
employees = [40, 25, 15, 10, 10]
pie = go.Figure(go.Pie(labels=departments, values=employees, hole=0.2))
pie.update_layout(title="Employee Distribution by Department")
save_figure(pie, "03_department_distribution_pie.html")

# 4. Scatter plot: study hours versus exam marks
student_names = [f"Student {number}" for number in range(1, 16)]
study_hours = [2, 3, 4, 5, 5, 6, 7, 7, 8, 9, 10, 10, 11, 12, 14]
exam_marks = [48, 52, 58, 61, 65, 68, 72, 75, 78, 82, 85, 88, 91, 94, 97]
scatter = go.Figure(go.Scatter(
    x=study_hours,
    y=exam_marks,
    mode="markers",
    text=student_names,
    hovertemplate="%{text}<br>Hours: %{x}<br>Marks: %{y}<extra></extra>",
    name="Students",
    marker={"size": 11, "color": exam_marks, "colorscale": "Viridis", "showscale": True},
))
scatter.update_layout(title="Study Hours and Exam Marks", xaxis_title="Hours Studied", yaxis_title="Exam Marks")
save_figure(scatter, "04_study_hours_scatter.html")

# 5. Histogram: 500 generated values
rng = np.random.default_rng(42)
random_values = rng.normal(loc=50, scale=12, size=500)
histogram = go.Figure(go.Histogram(x=random_values, nbinsx=25, name="Values", marker_color="#7c3aed"))
histogram.update_layout(title="Distribution of 500 Random Values", xaxis_title="Value", yaxis_title="Frequency")
save_figure(histogram, "05_random_values_histogram.html")

# 6. Box plot: salary distribution
salaries = [32000, 35000, 37000, 39000, 41000, 43000, 45000, 46000, 48000, 50000,
            52000, 54000, 56000, 58000, 60000, 62000, 64000, 66000, 68000, 70000,
            72000, 74000, 76000, 78000, 80000, 83000, 86000, 90000, 95000, 110000]
box = go.Figure(go.Box(y=salaries, name="Employees", boxmean=True, marker_color="#059669"))
box.update_layout(title="Employee Salary Distribution", xaxis_title="Employee Group", yaxis_title="Annual Salary (Rs.)")
save_figure(box, "06_salary_box_plot.html")

# 7. Multiple categories: product sales across months
product_sales = {
    "Laptop": [80, 95, 110, 100, 125, 140],
    "Mobile": [120, 135, 150, 145, 165, 180],
    "Tablet": [55, 65, 70, 62, 82, 90],
}
products = go.Figure()
for product, values in product_sales.items():
    products.add_trace(go.Bar(x=months, y=values, name=product))
products.update_layout(
    title="Monthly Sales by Product Category",
    xaxis_title="Month",
    yaxis_title="Sales (units)",
    barmode="group",
)
save_figure(products, "07_product_category_sales.html")

# 8. Student performance: three subjects for 10 students
performance_students = [f"Student {number}" for number in range(1, 11)]
python_marks = [78, 85, 92, 67, 88, 73, 95, 60, 84, 91]
mathematics_marks = [82, 79, 90, 70, 86, 75, 93, 65, 80, 89]
data_science_marks = [80, 88, 94, 72, 90, 77, 96, 62, 85, 92]
performance = go.Figure()
for subject, values in {
    "Python": python_marks,
    "Mathematics": mathematics_marks,
    "Data Science": data_science_marks,
}.items():
    performance.add_trace(go.Bar(x=performance_students, y=values, name=subject))
performance.update_layout(
    title="Student Performance by Subject",
    xaxis_title="Student",
    yaxis_title="Marks",
    barmode="group",
)
save_figure(performance, "08_student_performance.html")

# 9. 3D scatter: age, salary, and experience
ages = [22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 23, 27, 31, 35, 39, 25, 29, 33, 37, 41, 42, 44, 45, 46, 48, 50, 52, 43, 47, 49]
experience = [1, 2, 3, 4, 6, 7, 9, 10, 12, 15, 1, 4, 7, 10, 13, 2, 5, 8, 11, 16, 17, 19, 20, 21, 23, 25, 27, 18, 22, 24]
salary_3d = [30000, 34000, 38000, 42000, 50000, 56000, 62000, 68000, 74000, 85000,
             32000, 45000, 57000, 69000, 78000, 36000, 49000, 60000, 72000, 88000,
             92000, 100000, 108000, 112000, 125000, 140000, 155000, 105000, 120000, 132000]
scatter_3d = go.Figure(go.Scatter3d(
    x=ages,
    y=salary_3d,
    z=experience,
    mode="markers",
    text=[f"Employee {number}" for number in range(1, 31)],
    hovertemplate="%{text}<br>Age: %{x}<br>Salary: Rs. %{y}<br>Experience: %{z} years<extra></extra>",
    marker={"size": 5, "color": experience, "colorscale": "Plasma", "showscale": True},
    name="Employees",
))
scatter_3d.update_layout(
    title="Age, Salary, and Experience - 3D Scatter",
    scene={
        "xaxis_title": "Age (years)",
        "yaxis_title": "Salary (Rs.)",
        "zaxis_title": "Experience (years)",
    },
)
save_figure(scatter_3d, "09_employee_3d_scatter.html")

# 10. Custom graph: website traffic by channel
channels = ["Organic Search", "Social Media", "Email", "Referral", "Direct"]
visitors = [4200, 2800, 1900, 1600, 3500]
custom = go.Figure(go.Bar(x=channels, y=visitors, name="Visitors", marker_color="#ea580c"))
custom.update_layout(title="Website Visitors by Acquisition Channel", xaxis_title="Acquisition Channel", yaxis_title="Visitors")
save_figure(custom, "10_custom_website_traffic.html")

# 11. NumPy + Plotly: 100 random numbers
numpy_values = rng.integers(10, 101, size=100)
numpy_plot = go.Figure(go.Scatter(
    x=np.arange(1, 101),
    y=numpy_values,
    mode="lines+markers",
    name="NumPy values",
    line_color="#0891b2",
))
numpy_plot.update_layout(title="100 Random Numbers Generated with NumPy", xaxis_title="Position", yaxis_title="Random Value")
save_figure(numpy_plot, "11_numpy_random_numbers.html")

# 12. Dashboard thinking: four separate business charts in one dashboard
months_extended = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [120, 150, 170, 140, 200, 230]
expenses = [80, 95, 110, 100, 125, 140]
employee_count = [42, 43, 44, 45, 47, 49]
customer_count = [800, 920, 1050, 1010, 1240, 1400]
dashboard = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=("Revenue", "Expenses", "Employees", "Customers"),
)
dashboard.add_trace(go.Scatter(x=months_extended, y=revenue, mode="lines+markers", name="Revenue"), row=1, col=1)
dashboard.add_trace(go.Bar(x=months_extended, y=expenses, name="Expenses"), row=1, col=2)
dashboard.add_trace(go.Scatter(x=months_extended, y=employee_count, mode="lines+markers", name="Employees"), row=2, col=1)
dashboard.add_trace(go.Bar(x=months_extended, y=customer_count, name="Customers"), row=2, col=2)
dashboard.update_xaxes(title_text="Month", row=1, col=1)
dashboard.update_xaxes(title_text="Month", row=1, col=2)
dashboard.update_xaxes(title_text="Month", row=2, col=1)
dashboard.update_xaxes(title_text="Month", row=2, col=2)
dashboard.update_yaxes(title_text="Revenue (Rs. thousands)", row=1, col=1)
dashboard.update_yaxes(title_text="Expenses (Rs. thousands)", row=1, col=2)
dashboard.update_yaxes(title_text="Employees", row=2, col=1)
dashboard.update_yaxes(title_text="Customers", row=2, col=2)
dashboard.update_layout(title="Fictional Company Business Dashboard", height=800, showlegend=True)
save_figure(dashboard, "12_business_dashboard.html")

print(f"\nCreated {len(list(OUTPUT_DIR.glob('*.html')))} interactive HTML charts in {OUTPUT_DIR}")
